from flask import Flask, url_for


app = Flask(__name__)


@app.route("/")
@app.route("/image_mars")
def index():
    return f"""<!doctype html>
                 <html lang='en'
                   <head>
                   <!-- CSS only -->
                     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" 
                     rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" 
                     crossorigin="anonymous">
                     <title>Пейзажи</title>
                   </head>
                   <body>
                     <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                       <div class="carousel-inner">
                         <div class="carousel-item active">
                           <img class="d-block w-100" src="{url_for('static', filename='img/slide_1.jpg')}" alt="First slide">
                         </div>
                       </div>
                       <div class="carousel-inner">
                         <div class="carousel-item active">
                           <img class="d-block w-100" src="{url_for('static', filename='img/slide_2.jpg')}" alt="Second slide">
                         </div>
                       </div>
                       <div class="carousel-inner">
                         <div class="carousel-item active">
                           <img class="d-block w-100" src="{url_for('static', filename='img/slide_3.jpg')}" alt="Third slide">
                         </div>
                       </div>
                     </div>
                       
                     </div>  
                   </body
                 </html>
            """


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)