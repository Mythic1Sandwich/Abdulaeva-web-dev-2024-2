from flask import Flask

app = Flask(__name__) #создаем экземляр класса Flask
application = app
@app.route('/')
def index():
    return 'Hello, World!'