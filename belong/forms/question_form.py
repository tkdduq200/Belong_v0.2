from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


REQUIRED_MSG = "이 필드는 필수 입력 항목입니다."


class QuestionForm(FlaskForm):
    subject = StringField(
        "제목",
        validators=[
            DataRequired(REQUIRED_MSG),
            Length(min=1, max=200),
        ],
    )
    content = TextAreaField(
        "내용",
        validators=[DataRequired(REQUIRED_MSG)],
    )
    
