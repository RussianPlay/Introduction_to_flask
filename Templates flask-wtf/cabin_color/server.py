from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/table/<sex>/<int:age>")
def index(sex, age):
    return render_template("wall_picture.html", sex=sex, age=age)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
