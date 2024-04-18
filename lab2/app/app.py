
from flask import Flask, render_template, make_response, request
import verification as validator
app = Flask(__name__)
@app.route("/")
def index():
    url = request.url
    title = "Lab2"
    return render_template("index.html", title=title, url=url)

@app.route("/headers")
def headers():
    title = "HEADER"
    return render_template("headers.html", title=title, request=request)
@app.route("/cookies")
def cookies():
    title = "COOKIES"
    return render_template("cookies.html", title=title, request=request)
@app.route("/url")
def url():
    title = "Параметры URL"
    return render_template("url.html", title=title, request=request)

@app.route("/parameters", methods=["GET", "POST"])
def parameters():
    title = "ПАРАМЕТРЫ ФОРМЫ"
    return render_template("parameters.html", title=title, request=request)

@app.route("/phone", methods=["GET", "POST"])
def phone():
    title = "ВЕРИФИКАЦИЯ ПО ШАБЛОНУ"
    if request.method == "GET":
        return render_template("phone.html", title=title)

    phone = request.form.get("phone", "")
    flag = validator.validate(phone)
    if flag:
        return render_template("phone.html", title=title, request=request, checked=True, error=flag)
    else:
        phone = validator.formats(phone)
        return render_template("phone.html", title=title, request=request, checked=True, formatted=phone)
