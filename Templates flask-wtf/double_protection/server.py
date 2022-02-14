from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, url_for, redirect


app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


class LoginForm(FlaskForm):
    astro_id = StringField("id астронавта", validators=[DataRequired()])
    astro_password = PasswordField("пароль астронавта", validators=[DataRequired()])
    cap_id = StringField("id капитана", validators=[DataRequired()])
    cap_password = PasswordField("пароль капитана", validators=[DataRequired()])
    submit = SubmitField("Доступ")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return success([(form.astro_id.data, form.astro_password.data), (form.cap_id.data, form.cap_password.data)])
    return render_template("login.html", title="Авторизация", form=form)


@app.route("/success")
def success(data):
    print(data)
    return "Регистрация завершена"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

