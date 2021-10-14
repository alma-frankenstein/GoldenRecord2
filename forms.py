from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Length


class EmptyForm(FlaskForm):
    submit = SubmitField('submit')

class PostForm(FlaskForm):
    song = TextAreaField('song name', validators=[DataRequired(), Length(min=1, max=60)])
    artist = TextAreaField('artist name', validators=[DataRequired(), Length(min=1, max=60)])
    song_link = TextAreaField('link to song (optional)')
    submit = SubmitField('submit')
