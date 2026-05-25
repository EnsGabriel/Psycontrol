from app import db
from app.models.session import Session
from app.models.patient import Patient
from datetime import datetime


def get_all_sessions():
    return Session.query.order_by(Session.date.desc()).all()


def get_sessions_by_patient(patient_id):
    return Session.query.filter_by(patient_id=patient_id).order_by(Session.date.desc()).all()


def create_session(patient_id, date_str, notes):
    if not patient_id:
        return None, "Paciente é obrigatório."
    if not Patient.query.get(patient_id):
        return None, "Paciente não encontrado."
    if not date_str:
        return None, "Data é obrigatória."

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None, "Data inválida."

    session = Session(patient_id=patient_id, date=date, notes=notes)
    db.session.add(session)
    db.session.commit()
    return session, None


def delete_session(session_id):
    session = Session.query.get_or_404(session_id)
    db.session.delete(session)
    db.session.commit()


def update_session(session_id, patient_id, date_str, notes):
    session = Session.query.get_or_404(session_id)
    if not patient_id:
        return None, "Paciente é obrigatório."
    if not Patient.query.get(patient_id):
        return None, "Paciente não encontrado."
    if not date_str:
        return None, "Data é obrigatória."
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None, "Data inválida."

    session.patient_id = patient_id
    session.date = date
    session.notes = notes
    db.session.commit()
    return session, None


def get_session_by_id(session_id):
    return Session.query.get_or_404(session_id)
