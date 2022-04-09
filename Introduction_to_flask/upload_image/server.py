from flask import Flask, url_for, request, render_template


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    if request.method == "GET":
        return get_form_design()
    elif request.method == "POST":
        with open("static/img/buffer_img.jpg", "wb") as total_image:
            total_image.write(request.files['file'].read())
        return get_form_design()


def get_form_design():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")