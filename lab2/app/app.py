from random import randint
from flask import Flask, render_template, make_response, request
import phone_check as phonecheck

app = Flask(__name__)

@app.route("/")
def index():
    url = request.url
    title = "Lab1"
    return render_template("index.html", title=title, url=url)


@app.route("/URLparameters")
def URLparameters():
    title = "Параметры URL"
    return render_template("URLparameters.html", title=title, request=request)

@app.route("/headers")
def headers():
    title = "Параметры URL"
    return render_template("headers.html", title=title, request=request)

@app.route("/cookie")
def cookie():
    title = "Параметры URL"
    response = make_response(render_template(
        "cookie.html", title=title, request=request))
    if "cookie" in request.cookies:
        response.delete_cookie("cookie")
    else:
        response.set_cookie("cookie", "1")

    return response

@app.route("/formparameters", methods=["GET", "POST"])
def formparameters():
    title = "Параметры Формы"
    return render_template("formparameters.html", title=title, request=request)

@app.route("/phoneform", methods=["GET", "POST"])
def phoneform():
    title = "Проверка номера Телефона"
    if request.method == "GET":
        return render_template("phoneform.html", title=title)
    
    phone = request.form.get("phone", "")
    phoneCheckResult = phonecheck.phonecheck(phone)

    if not phoneCheckResult:
        phone = phonecheck.formatphone(phone)
        return render_template("phoneform.html", title=title, request=request, phoneChecked=True, formattedPhone=phone)
    else:
        return render_template("phoneform.html", title=title, request=request, phoneChecked=True, error=phoneCheckResult)