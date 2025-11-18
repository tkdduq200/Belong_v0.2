from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


REQUIRED_MSG = "이 필드는 필수 입력 항목입니다."
PASSWORD_NOT_MATCH_MSG = "비밀번호가 서로 일치하지 않습니다."
INVALID_EMAIL_MSG = "유효한 이메일 주소를 입력해주세요."


class UserCreateForm(FlaskForm):
    username = StringField(
        "사용자이름",
        validators=[
            DataRequired(REQUIRED_MSG),
            Length(min=3, max=25),
        ],
    )
    password1 = PasswordField(
        "비밀번호",
        validators=[
            DataRequired(REQUIRED_MSG),
            EqualTo("password2", message=PASSWORD_NOT_MATCH_MSG),
        ],
    )
    password2 = PasswordField(
        "비밀번호 확인",
        validators=[DataRequired(REQUIRED_MSG)],
    )
    email = StringField(
        "이메일",
        validators=[DataRequired(REQUIRED_MSG), Email(message=INVALID_EMAIL_MSG)],
    )


class UserLoginForm(FlaskForm):
    username = StringField(
        "사용자이름",
        validators=[
            DataRequired(REQUIRED_MSG),
            Length(min=3, max=25),
        ],
    )
    password = PasswordField(
        "비밀번호",
        validators=[DataRequired(REQUIRED_MSG)],
    )
