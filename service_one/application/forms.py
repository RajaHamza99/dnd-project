from flask_wtf import FlaskForm
from wtforms import SubmitField

class GenerateForm(FlaskForm):
    submit = SubmitField('Generate Character')
