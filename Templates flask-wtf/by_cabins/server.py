from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/distribution")
def index():
    astronauts = ["Эльмир", "Алексей", "Максим"]
    return render_template("placement_scheme.html", actronauts=astronauts)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
