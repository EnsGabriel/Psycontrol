from app import db


class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    birth_date = db.Column(db.Date, nullable=True)
    sessions = db.relationship("Session", backref="patient", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Patient {self.name}>"
