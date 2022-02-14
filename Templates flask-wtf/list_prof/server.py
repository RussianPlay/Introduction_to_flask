from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/list_prof/<listf>")
def index(listf):
    specs = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач" "инженер по терраформированию",
             "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог",
             "инженер жизнеобеспечения", "метеоролог", "оператор марсохода", "киберинженер", "штурман", "пилот дронов"]
    if "ol" in listf or "ul" in listf:
        return render_template("base.html", specs=specs, lst_format=listf)
    else:
        return "Неверный формат"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")