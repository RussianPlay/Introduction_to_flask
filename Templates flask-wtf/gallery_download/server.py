from flask import Flask, url_for, render_template, request
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/image_mars", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        ind = 0
        while os.path.exists(f"static/img/im{ind}.jpg"):
            ind += 1
        return render_template("im_carousel.html", ind=ind)
    elif request.method == "POST":
        ind = 0
        while os.path.exists(f"static/img/im{ind}.jpg"):
            ind += 1
        with open(f"static/img/im{ind}.jpg", "wb") as total_image:
            total_image.write(request.files["file"].read())
        ind += 1
        return render_template("im_carousel.html", ind=ind)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")