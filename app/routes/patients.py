from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from app.services.patient_service import (
    get_all_patients, get_patient_by_id, create_patient,
    delete_patient, update_patient
)
from app.services.session_service import get_sessions_by_patient

patients_bp = Blueprint("patients", __name__, url_prefix="/patients")


@patients_bp.route("/")
@login_required
def list_patients():
    patients = get_all_patients()
    return render_template("patients/list.html", patients=patients)


@patients_bp.route("/new", methods=["GET", "POST"])
@login_required
def new_patient():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        cpf = request.form.get("cpf", "").strip()
        phone = request.form.get("phone", "").strip()
        birth_date = request.form.get("birth_date", "").strip()
        patient, error = create_patient(name, cpf, phone, birth_date)
        if error:
            flash(error, "danger")
            return render_template("patients/form.html", patient=None)
        flash("Paciente cadastrado com sucesso!", "success")
        return redirect(url_for("patients.list_patients"))
    return render_template("patients/form.html", patient=None)


@patients_bp.route("/<int:patient_id>/edit", methods=["GET", "POST"])
@login_required
def edit_patient(patient_id):
    patient = get_patient_by_id(patient_id)
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        cpf = request.form.get("cpf", "").strip()
        phone = request.form.get("phone", "").strip()
        birth_date = request.form.get("birth_date", "").strip()
        patient, error = update_patient(patient_id, name, cpf, phone, birth_date)
        if error:
            flash(error, "danger")
            return render_template("patients/form.html", patient=patient)
        flash("Paciente atualizado com sucesso!", "success")
        return redirect(url_for("patients.detail", patient_id=patient_id))
    return render_template("patients/form.html", patient=patient)


@patients_bp.route("/<int:patient_id>")
@login_required
def detail(patient_id):
    patient = get_patient_by_id(patient_id)
    sessions = get_sessions_by_patient(patient_id)
    return render_template("patients/detail.html", patient=patient, sessions=sessions)


@patients_bp.route("/<int:patient_id>/delete", methods=["POST"])
@login_required
def delete(patient_id):
    delete_patient(patient_id)
    flash("Paciente removido.", "info")
    return redirect(url_for("patients.list_patients"))
