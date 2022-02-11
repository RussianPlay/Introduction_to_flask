from flask import Flask, url_for, render_template
import json


app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
