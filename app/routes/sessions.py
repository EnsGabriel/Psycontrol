from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from app.services.session_service import (
    get_all_sessions, create_session, delete_session,
    update_session, get_session_by_id
)
from app.services.patient_service import get_all_patients

sessions_bp = Blueprint("sessions", __name__, url_prefix="/sessions")


@sessions_bp.route("/")
@login_required
def list_sessions():
    sessions = get_all_sessions()
    return render_template("sessions/list.html", sessions=sessions)


@sessions_bp.route("/new", methods=["GET", "POST"])
@login_required
def new_session():
    patients = get_all_patients()
    if request.method == "POST":
        patient_id = request.form.get("patient_id", type=int)
        date = request.form.get("date", "").strip()
        notes = request.form.get("notes", "").strip()
        session, error = create_session(patient_id, date, notes)
        if error:
            flash(error, "danger")
            return render_template("sessions/form.html", patients=patients, session=None)
        flash("Sessão registrada com sucesso!", "success")
        return redirect(url_for("sessions.list_sessions"))
    return render_template("sessions/form.html", patients=patients, session=None)


@sessions_bp.route("/<int:session_id>/edit", methods=["GET", "POST"])
@login_required
def edit_session(session_id):
    session = get_session_by_id(session_id)
    patients = get_all_patients()
    if request.method == "POST":
        patient_id = request.form.get("patient_id", type=int)
        date = request.form.get("date", "").strip()
        notes = request.form.get("notes", "").strip()
        session, error = update_session(session_id, patient_id, date, notes)
        if error:
            flash(error, "danger")
            return render_template("sessions/form.html", patients=patients, session=session)
        flash("Sessão atualizada com sucesso!", "success")
        return redirect(url_for("sessions.list_sessions"))
    return render_template("sessions/form.html", patients=patients, session=session)


@sessions_bp.route("/<int:session_id>/delete", methods=["POST"])
@login_required
def delete(session_id):
    delete_session(session_id)
    flash("Sessão removida.", "info")
    return redirect(url_for("sessions.list_sessions"))
