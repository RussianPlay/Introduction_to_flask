from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/list_prof/<list>")
def index(lst_format):
    specs = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач" "инженер по терраформированию",
             "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог",
             "инженер жизнеобеспечения", "метеоролог", "оператор марсохода", "киберинженер", "штурман", "пилот дронов"]
    if "ol" in lst_format or "ul" in lst_format:
        return render_template("b.html", specs=specs, lst_format=lst_format)
    else:
        return "Неверный формат"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")