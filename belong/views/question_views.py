from flask import Blueprint, render_template, request, url_for, abort
from werkzeug.utils import redirect

from ..forms import QuestionForm, AnswerForm
from ..services import QuestionService
from ..repositories.question_repository import QuestionRepository

bp = Blueprint("question", __name__, url_prefix="/question")

# Service 인스턴스 (간단 DI)
_question_service = QuestionService(QuestionRepository())


@bp.route("/list/")
def _list():
    page = request.args.get("page", type=int, default=1)
    question_list = _question_service.get_question_list(page=page, per_page=10)
    return render_template(
        "question/question_list.html",
        question_list=question_list,
    )


@bp.route("/detail/<int:question_id>/")
def detail(question_id):
    form = AnswerForm()
    question = _question_service.get_question(question_id)
    if question is None:
        abort(404)

    return render_template(
        "question/question_detail.html",
        question=question,
        form=form,
    )


@bp.route("/create/", methods=["GET", "POST"])
def create():
    form = QuestionForm()

    if request.method == "POST" and form.validate_on_submit():
        _question_service.create_question(
            subject=form.subject.data,
            content=form.content.data,
        )
        return redirect(url_for("main.index"))

    return render_template("question/question_form.html", form=form)
