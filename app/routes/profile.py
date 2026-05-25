from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash
from app import db

profile_bp = Blueprint("profile", __name__, url_prefix="/profile")


@profile_bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        current_password = request.form.get("current_password", "")
        new_password = request.form.get("new_password", "")

        if not name:
            flash("Nome é obrigatório.", "danger")
            return render_template("profile/index.html")

        current_user.name = name

        if current_password or new_password:
            if not current_user.check_password(current_password):
                flash("Senha atual incorreta.", "danger")
                return render_template("profile/index.html")
            if len(new_password) < 6:
                flash("Nova senha deve ter no mínimo 6 caracteres.", "danger")
                return render_template("profile/index.html")
            current_user.set_password(new_password)

        db.session.commit()
        flash("Perfil atualizado com sucesso!", "success")
        return redirect(url_for("profile.index"))

    return render_template("profile/index.html")
