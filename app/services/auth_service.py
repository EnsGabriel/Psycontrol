from app import db
from app.models.user import User


def register_user(name, email, password):
    if len(password) < 6:
        return None, "A senha deve ter no mínimo 6 caracteres."
    if User.query.filter_by(email=email).first():
        return None, "E-mail já cadastrado."
    user = User(name=name, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user, None


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return None, "E-mail ou senha inválidos."
    return user, None
