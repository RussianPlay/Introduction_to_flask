from flask import Flask, url_for


app = Flask(__name__)


@app.route("/")
def show_title():
    return """<!doctype html>
                <html lang='en'
                  <head>
                    <title>Миссия Колонизация Марса</title>
                  </head>
                </html>
           """


@app.route("/index")
def index():
    return """<!doctype html>
                <html lang='en'
                  <head>
                    <title>Миссия Колонизация Марса</title>
                  </head>
                  <body>
                    <h1><b>И на Марсе будут яблони цвести!</b></title>
                  </body
                </html>
           """


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")