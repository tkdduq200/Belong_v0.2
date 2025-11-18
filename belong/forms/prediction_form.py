from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired


class PredictionForm(FlaskForm):
    gu = SelectField(
        "구",
        choices=[],
        validators=[DataRequired()],
    )
    year = SelectField(
        "연도",
        choices=[],
        validators=[DataRequired()],
    )
