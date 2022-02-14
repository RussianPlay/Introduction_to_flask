from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/answer")
@app.route("/auto_answer")
def index():
    params = dict()
    params["title"] = "Миссия Колонизация М1"
    params["surname"] = "Ahmadullin"
    params["name"] = "Elmir"
    params["education"] = "Megabrain"
    params["profession"] = "programmist"
    params["sex"] = "male"
    params["motivation"] = "live in space"
    params["ready"] = True
    return render_template("auto_answer.html", **params)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
