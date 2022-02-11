from flask import Flask, url_for


app = Flask(__name__)


@app.route("/")
def show_title():
    return """<!doctype html>
                <html lang='en'
                  <head>
                    <title>Рекламная кампания</title>
                  </head>
                </html>
           """


@app.route("/promotion")
def promotion():
    text = ["Человечество вырастает из детства.",
            "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.",
            "И начнем с Марса!", "Присоединяйся!"]
    return f"""<!doctype html>
                 <html lang='en'
                   <head>
                     <title>Рекламная кампания</title>
                   </head>
                   <body>
                     {"<br>".join(map(lambda row: f'<h1><b>{row}</b></title>', text))}
                   </body
                 </html>
            """


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")