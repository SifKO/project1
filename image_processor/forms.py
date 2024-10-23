"""
Form that I used in project
"""

from flask_wtf import RecaptchaField, FlaskForm
from flask_wtf.file import FileField, FileRequired
from matplotlib.offsetbox import TextArea
from wtforms import StringField, TextAreaField, validators
from wtforms.validators import Length
from werkzeug.utils import secure_filename


class ImgProcessForm(FlaskForm):
    """
    Download File
    Capcha field
    """
    photo = FileField(validators=[FileRequired()])
    recapthca = RecaptchaField()

# class SlicePice():
#     """
#     Image 
#     """
#     def __init__(self, image, pieces):
#     text_area = TextArea
#     imge = 
