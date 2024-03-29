from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from forms.user import RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


@app.route("/register", methods=["GET", "POST"])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template("reg_form.html", title="Регистрация", form=form, message="Пароли не совпадают")
        db_session.global_init("db/user_data.db")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template("reg_form.html", title="Регистрация", form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect("/login")
    print(1)
    return render_template("reg_form.html", title="Регистрация", form=form)


@app.route("/login")
def login():
    return "Регистрация пройдена успешно"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
