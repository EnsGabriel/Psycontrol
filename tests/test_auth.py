from app.services.auth_service import register_user, authenticate_user


def test_register_user_success(app):
    user, error = register_user("Dr. João", "joao@test.com", "senha123")
    assert error is None
    assert user is not None
    assert user.email == "joao@test.com"


def test_register_user_duplicate_email(app):
    register_user("Dr. João", "joao@test.com", "senha123")
    user, error = register_user("Outro", "joao@test.com", "outrasenha")
    assert user is None
    assert "E-mail já cadastrado" in error


def test_register_user_short_password(app):
    user, error = register_user("Dr. João", "joao@test.com", "123")
    assert user is None
    assert "mínimo 6 caracteres" in error


def test_login_invalid_credentials(app):
    register_user("Dr. João", "joao@test.com", "senha123")
    user, error = authenticate_user("joao@test.com", "senhaerrada")
    assert user is None
    assert "inválidos" in error


def test_login_nonexistent_user(app):
    user, error = authenticate_user("naoexiste@test.com", "qualquer")
    assert user is None
    assert error is not None


def test_login_success(app):
    register_user("Dr. João", "joao@test.com", "senha123")
    user, error = authenticate_user("joao@test.com", "senha123")
    assert error is None
    assert user is not None
