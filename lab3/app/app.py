from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from functools import wraps

app = Flask(__name__)
app.secret_key = 'secret_key'

manager = LoginManager()
manager.init_app(app)

users = {'user': {'password': 'qwerty'}}

class User(UserMixin):
    def __init__(self, id):
        self.id = id
    
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

@app.route('/')
def index():
    session['visits'] = session.get('visits', 0) + 1
    return render_template('index.html', title='Главная страница')

@manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = request.form.get('remember')
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user, remember=remember)
            flash('Вы успешно вошли', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index')) 
        else:
            flash('Неверный логин или пароль', 'error')
    return render_template('auth.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно вышли из аккаунта', 'success')
    return redirect(url_for('auth'))

def auth_message(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Для доступа к запрашиваемой странице необходимо пройти процедуру аутентификации!', 'error')
            return redirect(url_for('auth', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/secret')
@auth_message
def secret():
    return render_template('secret.html', title='Секретная страница')

if __name__ == '__main__':
    app.run(debug=True)
