from flask import Flask, url_for, request


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def form_sample():
    if request.method == "GET":
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel='stylesheet' type='text/css' href='{url_for('static', filename='css/style.css')}' />
    
                        <title>Отбор астронавтов</title>
                      </head>
                      <body>
                        <h1>Анкета претендента</h1>
                        <h2>на участие в миссии</h1>
                        <div>
                          <form class='login_form' method='post'>
                            <input type='text' class='form-control' id='text' placeholder='Введите имя' name='surname'>
                            <input type='text' class='form-control' id='text' placeholder='Введите фамилию' name='name'>
                            <input type='email' class='form-control' aria-id='email' aria-describedly='paswordHelp' placeholder='Введите почту' name='email'>
                            <div class='form-group'>
                              <label for='classSelect'>Какое у вас образование</label>
                              <select class='form-control' id='classSelect' name='class'>
                                <option>Начальное</option>
                                <option>Среднее</option>
                                <option>Высшее</option>
                                <option>Мегамозг</option>
                              </select>
                            </div>
                            <div class="form-group">
                              <label for="form-check">Какие у Вас есть професии</label>
                              <div class="form-check">
                                <input class="form-check-input" type="checkbox" name="ing-s" value="ing-s" id="ing-s">
                                <label class="form-check-label" for="ing-b">
                                  Инженер-исследователь
                                </label>
                              </div>
                              <div class="form-check">
                                <input class="form-check-input" type="checkbox" name="ing-b" value="ing-b" id="ing-b">
                                <label class="form-check-label" for="ing-b">
                                  Инженер-строитель
                                </label>
                              </div>
                              <div class="form-check" >
                                <input class="form-check-input" type="checkbox" name="pil" value="pil" id="pil">
                                <label class="form-check-label" for="pil">
                                  Пилот
                                </label>
                              </div>
                            </div>
                            <div class="form-group">
                              <label for="form-check">Укажите пол</label>
                              <div class="form-check">
                                <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                <label class="form-check-label" for="male">
                                  Мужской
                                </label>
                              </div>
                              <div class="form-check">
                                <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                <label class="form-check-label" for="female">
                                  Женский
                                </label>
                              </div>
                            </div>
                            <div class='form-group'>
                              <label for='about'>Почему вы хотите принять участие в миссии?</label>
                              <textarea class='form-control' id='about' rows='3' name='about'></textarea>
                            </div>
                            <div>
                                <form encype="multipart/form-data" method="post">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                      <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                      <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </form>
                          
                        </div>
                      </body>
                    </html>'''
    elif request.method == "POST":
        print(request.form["name"])
        print(request.form["surname"])
        print(request.form["email"])
        print(request.form.get("class"))
        print(request.form.get("ing-s"), request.form.get("ing-b"), request.form.get("pil"))
        print(request.form["sex"])
        print(request.form["about"])
        print(request.form["file"])
        print(request.form.get("accept"))
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)