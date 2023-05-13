import random
import string

from flask import Flask, render_template, redirect, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class URLForm(FlaskForm):
    url = StringField("Ссылка", validators=[
        DataRequired(message='Поле "Ссылка" не может быть пустым'),
        URL(message="Ссылка введена не верно")
    ])
    submit = SubmitField("Сократить ссылку")


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"

db = SQLAlchemy(app)


class URLS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(40), unique=True, nullable=False)
    visits = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime, default=datetime.utcnow())


with app.app_context():
    db.create_all()


def get_short():
    while True:
        short = "".join(random.choices(string.ascii_letters + string.ascii_letters + string.digits, k=6))

        if URLS.query.filter(URLS.short == short).first():
            continue
        else:
            return short


def index():
    form = URLForm()

    if form.validate_on_submit():
        urls_model = URLS()

        urls_model.url = form.url.data
        urls_model.short = get_short()

        db.session.add(urls_model)
        db.session.commit()

        return redirect(url_for("urls"))

    return render_template("index.html", form=form)


def urls():
    urls_list = URLS.query.order_by(URLS.date.desc()).all()

    return render_template("urls.html", urls=urls_list)


def url_redirect(short):
    url_model = URLS.query.filter(URLS.short == short).first()

    if url_model:
        url_model.visits += 1

        db.session.add(url_model)
        db.session.commit()

        return redirect(url_model.url)

    return "Такой короткой ссылки нет!"


app.add_url_rule("/", "index", index, methods=["GET", "POST"])
app.add_url_rule("/urls", "urls", urls)
app.add_url_rule("/<string:short>", "url_redirect", url_redirect)
