from flask import Blueprint, render_template
from flask_login import login_required
from app.models.patient import Patient
from app.models.session import Session

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
@login_required
def index():
    total_patients = Patient.query.count()
    total_sessions = Session.query.count()
    recent_sessions = Session.query.order_by(Session.date.desc()).limit(5).all()
    return render_template(
        "dashboard/index.html",
        total_patients=total_patients,
        total_sessions=total_sessions,
        recent_sessions=recent_sessions,
    )
