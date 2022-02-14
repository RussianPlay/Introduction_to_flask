from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/<spec>")
@app.route("/training/<spec>")
def index(spec):
    if "инженер" in spec.lower() or "строитель" in spec.lower():
        return render_template("b.html", training="Инженерные тренажеры")
    elif "науч" in spec.lower():
        return render_template("b.html", training="Научные симуляторы")
    return render_template("index.html", training="Другие симуляторы")


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")