from flask import Flask, url_for


app = Flask(__name__)


@app.route("/")
def show_title():
    return """<!doctype html>
                <html lang='en'
                  <head>
                    <title>Результаты</title>
                  </head>
                </html>
           """


@app.route("/choice/<nickname>/<level>/<rating>")
def promotion(nickname, level, rating):
    try:
        level = int(level)
        rating = float(rating)
    except ValueError:
        return "Неправильные данные"

    return f"""<!doctype html>
                 <html lang='en'
                   <head>
                     <link rel="stylesheet" 
                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                     integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                     crossorigin="anonymous">
                     <title>Результаты</title>
                   </head>
                   <body>
                     <h1><b>>Результаты выбора</b></h1>
                     <h2>Претендента на участие в миссии {nickname}:<h2>
                     <div class='alert alert-success' role='alert'>
                       Поздравляем! Ваш рейтинг после {level} этапа отбора
                     </div>
                     <h2>Составляет {float(rating)}!<h2>
                     <div class='alert alert-warning' role='alert'>
                       Желаем удачи!
                     </div>
                   </body
                 </html>
            """


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
