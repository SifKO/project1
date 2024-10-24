"""
Form that I used in project
"""

from flask_wtf import RecaptchaField, FlaskForm
from flask_wtf.file import FileField, FileRequired


class ImgProcessForm(FlaskForm):
    """
    Download File
    Capcha field
    """
    photo = FileField(validators=[FileRequired()])
    recapthca = RecaptchaField()
