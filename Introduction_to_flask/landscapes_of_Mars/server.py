from flask import Flask, url_for, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/image_mars")
def index():
    return render_template("im_carousel.html")


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")