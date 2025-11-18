from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired


REQUIRED_MSG = "이 필드는 필수 입력 항목입니다."


class AnswerForm(FlaskForm):
    content = TextAreaField(
        "내용",
        validators=[DataRequired(REQUIRED_MSG)],
    )
