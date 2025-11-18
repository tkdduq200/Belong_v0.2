from flask import (
    Blueprint,
    url_for,
    render_template,
    flash,
    request,
    session,
    g,
)
from werkzeug.utils import redirect

from ..forms import UserCreateForm, UserLoginForm
from ..services import UserService
from ..repositories.user_repository import UserRepository

bp = Blueprint("auth", __name__, url_prefix="/auth")

_user_service = UserService(UserRepository())


@bp.route("/signup/", methods=("GET", "POST"))
def signup():
    form = UserCreateForm()
    if request.method == "POST" and form.validate_on_submit():
        user, error = _user_service.register_user(
            username=form.username.data,
            email=form.email.data,
            raw_password=form.password1.data,
        )
        if error:
            flash(error)
        else:
            return redirect(url_for("main.index"))
    return render_template("auth/signup.html", form=form)


@bp.route("/login/", methods=("GET", "POST"))
def login():
    form = UserLoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user, error = _user_service.authenticate(
            username=form.username.data,
            raw_password=form.password.data,
        )

        if error:
            flash(error)
        else:
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for("main.index"))

    return render_template("auth/login.html", form=form)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = _user_service.get_user_by_id(user_id)


@bp.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for("main.index"))
