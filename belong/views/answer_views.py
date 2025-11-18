from flask import Blueprint, url_for, request, render_template, abort
from werkzeug.utils import redirect

from ..forms import AnswerForm
from ..services import AnswerService, QuestionService
from ..repositories.answer_repository import AnswerRepository
from ..repositories.question_repository import QuestionRepository

bp = Blueprint("answer", __name__, url_prefix="/answer")

# Service 인스턴스
_question_service = QuestionService(QuestionRepository())
_answer_service = AnswerService(AnswerRepository(), QuestionRepository())


@bp.route("/create/<int:question_id>", methods=("POST", "GET"))
def create(question_id):
    form = AnswerForm()
    question = _question_service.get_question(question_id)

    if question is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        answer = _answer_service.create_answer(question_id=question_id, content=content)
        if answer is None:
            abort(400)

        return redirect(url_for("question.detail", question_id=question_id))

    return render_template(
        "question/question_detail.html",
        question=question,
        form=form,
    )
