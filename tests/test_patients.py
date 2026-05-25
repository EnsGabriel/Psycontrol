from app.services.patient_service import create_patient, get_all_patients, delete_patient


def test_create_patient_success(app):
    patient, error = create_patient("Maria Silva", "123.456.789-00", "(49) 99999-0000", "1990-05-15")
    assert error is None
    assert patient is not None
    assert patient.name == "Maria Silva"


def test_create_patient_duplicate_cpf(app):
    create_patient("Maria Silva", "123.456.789-00", "", "")
    patient, error = create_patient("João Souza", "123.456.789-00", "", "")
    assert patient is None
    assert "CPF já cadastrado" in error


def test_create_patient_missing_name(app):
    patient, error = create_patient("", "111.111.111-11", "", "")
    assert patient is None
    assert "Nome é obrigatório" in error


def test_create_patient_missing_cpf(app):
    patient, error = create_patient("Maria Silva", "", "", "")
    assert patient is None
    assert "CPF é obrigatório" in error


def test_list_patients(app):
    create_patient("Ana", "111.111.111-11", "", "")
    create_patient("Carlos", "222.222.222-22", "", "")
    patients = get_all_patients()
    assert len(patients) == 2
