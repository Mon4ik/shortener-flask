from . import app, db

import string
import random

from flask import redirect, render_template, url_for

from .forms import URLForm
from .models import URLS


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
