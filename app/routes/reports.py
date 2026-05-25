from flask import Blueprint, render_template
from flask_login import login_required
from app.models.patient import Patient
from app.models.session import Session
from sqlalchemy import func
from app import db

reports_bp = Blueprint("reports", __name__, url_prefix="/reports")


@reports_bp.route("/")
@login_required
def index():
    total_patients = Patient.query.count()
    total_sessions = Session.query.count()

    # Sessões por paciente
    sessions_per_patient = (
        db.session.query(Patient.name, func.count(Session.id).label("total"))
        .join(Session, Session.patient_id == Patient.id)
        .group_by(Patient.id)
        .order_by(func.count(Session.id).desc())
        .all()
    )

    # Sessões por mês (últimos 6 meses)
    sessions_by_month = (
        db.session.query(
            func.strftime("%Y-%m", Session.date).label("month"),
            func.count(Session.id).label("total")
        )
        .group_by(func.strftime("%Y-%m", Session.date))
        .order_by(func.strftime("%Y-%m", Session.date).desc())
        .limit(6)
        .all()
    )

    # Pacientes sem sessão
    patients_no_session = (
        Patient.query.outerjoin(Session)
        .filter(Session.id == None)
        .all()
    )

    return render_template(
        "reports/index.html",
        total_patients=total_patients,
        total_sessions=total_sessions,
        sessions_per_patient=sessions_per_patient,
        sessions_by_month=list(reversed(sessions_by_month)),
        patients_no_session=patients_no_session,
    )
