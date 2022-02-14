from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/")
def index():
    astronauts = {"Эльмир": (["инженер-исследователь", "пилот", "строитель"], "marsianin_1.png"),
                  "Алексей": (["инженер жизнеобеспечения", "метеоролог", "оператор марсохода"], "marsianin_2.png"),
                  "Максим": (["штурман", "пилот дронов"], "marsianin_3.png")}
    return render_template("base.html", astronauts=astronauts)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")