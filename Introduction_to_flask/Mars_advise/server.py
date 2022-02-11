from flask import Flask, url_for


app = Flask(__name__)


@app.route("/")
def show_title():
    return """<!doctype html>
                <html lang='en'
                  <head>
                    <title>Колонизация</title>
                  </head>
                </html>
           """


@app.route("/promotion_image")
def promotion():
    return f"""<!doctype html>
                 <html lang='en'
                   <head>
                     <link rel="stylesheet" 
                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                     integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                     crossorigin="anonymous">
                     <link rel='stylesheet' type='text/css' href='{url_for('static', filename='css/style.css')}' />
                     <title>Колонизация</title>
                   </head>
                   <body>
                     <h1><b>Жди нас, Марс!</b></h1>
                     <img src='{url_for('static', filename='img/Mars.jpeg')}' alt='Изображение не нашлось'>
                     <div class='alert alert-primary' role='alert'>
                       Человечество вырастает из детства.
                     </div>
                     <div class='alert alert-secondary' role='alert'>
                       Человечеству мала одна планета.
                     </div>
                     <div class='alert alert-success' role='alert'>
                       Мы сделаем обитаемыми безжизненные пока планеты.
                     </div>
                     <div class='alert alert-danger' role='alert'>
                       И начнем с Марса!
                     </div>
                     <div class='alert alert-warning' role='alert'>
                       Присоединяйся!
                     </div>
                   </body
                 </html>
            """


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")