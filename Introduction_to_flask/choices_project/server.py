from flask import Flask, url_for


app = Flask(__name__)


@app.route("/")
def show_title():
    return """<!doctype html>
                <html lang='en'
                  <head>
                    <title>Варианты выбора</title>
                  </head>
                </html>
           """


@app.route("/choice/<planet_name>")
def promotion(planet_name):
    return f"""<!doctype html>
                 <html lang='en'
                   <head>
                     <link rel="stylesheet" 
                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                     integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                     crossorigin="anonymous">
                     <title>Варианты выбора</title>
                   </head>
                   <body>
                     <h1><b>Мое предложение: {planet_name}</b></h1>
                     <h2>Эта планета близка к Земле<h2>
                     <div class='alert alert-primary' role='alert'>
                       На ней много необходимых ресурсов
                     </div>
                     <div class='alert alert-secondary' role='alert'>
                       На ней есть вода и атмосфера
                     </div>
                     <div class='alert alert-success' role='alert'>
                       На ней есть небольшое магнитное поле
                     </div>
                     <div class='alert alert-danger' role='alert'>
                       Наконец, она просто красива!
                     </div>
                   </body
                 </html>
            """


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
