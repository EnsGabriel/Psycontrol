from app.services.patient_service import create_patient
from app.services.session_service import create_session, get_all_sessions


def test_create_session_success(app):
    patient, _ = create_patient("Maria", "123.456.789-00", "", "")
    session, error = create_session(patient.id, "2024-06-01", "Primeira sessão.")
    assert error is None
    assert session is not None
    assert session.patient_id == patient.id


def test_create_session_without_patient(app):
    session, error = create_session(None, "2024-06-01", "Notas")
    assert session is None
    assert "Paciente é obrigatório" in error


def test_create_session_invalid_patient(app):
    session, error = create_session(9999, "2024-06-01", "Notas")
    assert session is None
    assert "não encontrado" in error


def test_create_session_missing_date(app):
    patient, _ = create_patient("Maria", "123.456.789-00", "", "")
    session, error = create_session(patient.id, "", "Notas")
    assert session is None
    assert "Data é obrigatória" in error


def test_list_sessions(app):
    patient, _ = create_patient("Maria", "123.456.789-00", "", "")
    create_session(patient.id, "2024-06-01", "Sessão 1")
    create_session(patient.id, "2024-06-08", "Sessão 2")
    sessions = get_all_sessions()
    assert len(sessions) == 2
