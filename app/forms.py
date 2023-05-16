from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class URLForm(FlaskForm):
    url = StringField("Ссылка", validators=[
        DataRequired(message='Поле "Ссылка" не может быть пустым'),
        URL(message="Ссылка введена не верно")
    ])
    submit = SubmitField("Сократить ссылку")
