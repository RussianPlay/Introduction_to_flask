from flask import Flask, url_for


app = Flask(__name__)


@app.route("/")
def show_title():
    return """<!doctype html>
                <html lang='en'
                  <head>
                    <title>Привет, Марс!</title>
                  </head>
                </html>
           """


@app.route("/image_mars")
def promotion():
    return f"""<!doctype html>
                 <html lang='en'
                   <head>
                     <title>Привет, Марс!</title>
                   </head>
                   <body>
                     <h1><b>Жди нас, Марс!</b></h1>
                     <img src='{url_for('static', filename='img/Mars.jpeg')}' alt='Изображение не нашлось'>
                     <p>Вот какая, красная планета</p>
                   </body
                 </html>
            """


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")