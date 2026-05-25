from app import db
from app.models.patient import Patient
from datetime import datetime


def get_all_patients():
    return Patient.query.order_by(Patient.name).all()


def get_patient_by_id(patient_id):
    return Patient.query.get_or_404(patient_id)


def create_patient(name, cpf, phone, birth_date_str):
    if not name:
        return None, "Nome é obrigatório."
    if not cpf:
        return None, "CPF é obrigatório."
    if Patient.query.filter_by(cpf=cpf).first():
        return None, "CPF já cadastrado."

    birth_date = None
    if birth_date_str:
        try:
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        except ValueError:
            return None, "Data de nascimento inválida."

    patient = Patient(name=name, cpf=cpf, phone=phone, birth_date=birth_date)
    db.session.add(patient)
    db.session.commit()
    return patient, None


def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()


def update_patient(patient_id, name, cpf, phone, birth_date_str):
    patient = Patient.query.get_or_404(patient_id)
    if not name:
        return None, "Nome é obrigatório."
    if not cpf:
        return None, "CPF é obrigatório."
    existing = Patient.query.filter_by(cpf=cpf).first()
    if existing and existing.id != patient_id:
        return None, "CPF já cadastrado para outro paciente."

    birth_date = None
    if birth_date_str:
        try:
            from datetime import datetime
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        except ValueError:
            return None, "Data de nascimento inválida."

    patient.name = name
    patient.cpf = cpf
    patient.phone = phone
    patient.birth_date = birth_date
    db.session.commit()
    return patient, None
