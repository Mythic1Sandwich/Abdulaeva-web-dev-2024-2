from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from mysqldb import DBConnector
from mysql.connector.errors import DatabaseError
import re

app = Flask(__name__)
application = app
app.config.from_pyfile('config.py')

db_connector = DBConnector(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth"
login_manager.login_message = "Войдите, чтобы просматривать содержимое данной страницы"
login_manager.login_message_category = "warning"

class User(UserMixin):
    def __init__(self, user_id, login):
        self.id = user_id
        self.login = login

def get_user_list():
    return [{"user_id": "14", "login": "root", "password": "admin"}, 
            {"user_id": "64", "login": "guest", "password": "c1sc0"}, 
            {"user_id": "98", "login": "user", "password": "example"}]

CREATE_USER_FIELDS = ['login', 'password', 'name', 'last_name', 'surname', 'role_id']
EDIT_USER_FIELDS = ['last_name', 'name', 'surname', 'role_id']
CHANGE_PASS_FIELDS=['password','newpass','newpass2']
def get_roles():
    query = "SELECT * FROM roles"

    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute(query)
        roles = cursor.fetchall()

    return roles

@login_manager.user_loader
def load_user(user_id):
    query = "SELECT user_id, login FROM users WHERE user_id=%s"

    with db_connector.connect().cursor(named_tuple=True) as cursor:

        cursor.execute(query, (user_id,))
        
        user = cursor.fetchone()

    if user:
        return User(user_id, user.login)
    
    return None

    # for user_entry in get_user_list():
    #     if user_id == user_entry["user_id"]:
    #         return User(user_id, user_entry["login"])
    # return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    session['counter'] = session.get('counter', 0) + 1

    return render_template('info.html')

@app.route('/auth', methods=["GET", "POST"])
def auth():
    if request.method == "GET":
        return render_template("auth.html")
    
    login = request.form.get("login", "")
    password = request.form.get("pass", "")
    remember = request.form.get("remember") == "on"

    query = 'SELECT user_id, login FROM users WHERE login=%s AND password=SHA2(%s, 256)'
    
    print(query)

    with db_connector.connect().cursor(named_tuple=True) as cursor:

        cursor.execute(query, (login, password))

        print(cursor.statement)

        user = cursor.fetchone()

    if user:
        login_user(User(user.user_id, user.login), remember=remember)
        flash("Успешная авторизация", category="success")
        target_page = request.args.get("next", url_for("index"))
        return redirect(target_page)

    flash("Введены некорректные учётные данные пользователя", category="danger")    

    return render_template("auth.html")

@app.route('/users')
def users():
    query = 'SELECT users.*, roles.role_name FROM users LEFT JOIN roles ON users.role_id = roles.role_id'

    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute(query)
        data = cursor.fetchall() 
        print(data)

    return render_template("users.html", users=data)
   
def get_form_data(required_fields):
    user = {}

    for field in required_fields:
        user[field] = request.form.get(field) or None

    return user

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    query = ("SELECT * FROM users where user_id = %s")
    roles = get_roles()
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute(query, (user_id, ))
        user = cursor.fetchone()

    if request.method == "POST":
        user = get_form_data(EDIT_USER_FIELDS)
        user['user_id'] = user_id
        query = ("UPDATE users "
                 "SET last_name=%(last_name)s, name=%(name)s, "
                 "surname=%(surname)s, role_id=%(role_id)s "
                 "WHERE user_id=%(user_id)s ")

        try:
            with db_connector.connect().cursor(named_tuple=True) as cursor:
                cursor.execute(query, user)
                db_connector.connect().commit()
            
            flash("Запись пользователя успешно обновлена", category="success")
            return redirect(url_for('users'))
        except DatabaseError as error:
            flash(f'Ошибка редактирования пользователя! {error}', category="danger")
            db_connector.connect().rollback()    

    return render_template("edit_user.html", user=user, roles=roles)

@app.route('/users/<int:user_id>/seek', methods=['GET', 'POST'])
def seek(user_id):
    query = ("SELECT * FROM users where user_id = %s")
    queryw = 'SELECT roles.role_name FROM  roles JOIN users ON users.role_id = roles.role_id WHERE users.user_id=%s'
    with db_connector.connect().cursor(named_tuple=True) as roles:
        roles.execute(queryw, (user_id, ))
        role = roles.fetchall()
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute(query, (user_id, ))
        user = cursor.fetchone()
    return render_template("seek.html", user=user, role=role)

@app.route('/user/<int:user_id>/delete', methods=["POST"])
@login_required
def delete_user(user_id):
    query1 = "DELETE FROM users WHERE user_id=%s"
    try:
        with db_connector.connect().cursor(named_tuple=True) as cursor:
          
            cursor.execute(query1, (user_id, ))
            db_connector.connect().commit() 
        
        flash("Запись пользователя успешно удалена", category="success")
    except DatabaseError as error:
        flash(f'Ошибка удаления пользователя! {error}', category="danger")
        db_connector.connect().rollback()    
    
    return redirect(url_for('users'))


@app.route('/users/new', methods=['GET', 'POST'])
@login_required
def create_user():
    user = {}
    roles = get_roles()
    if request.method == 'POST':
        user = get_form_data(CREATE_USER_FIELDS)

        query = ("INSERT INTO users "
                 "(login, password, name, last_name, surname, role_id) "
                 "VALUES (%(login)s, SHA2(%(password)s, 256), "
                 "%(name)s, %(last_name)s,  %(surname)s, %(role_id)s)")
        if not user['login']:
            flash("Логин не может быть пустым", category="danger")
            return render_template("user_form.html", user=user, roles=roles)
        if not user['name']:
            flash("Имя не может быть пустым", category="danger")
            return render_template("user_form.html", user=user, roles=roles)
        if not user['surname']:
            flash("Отчество не может быть пустым", category="danger")
            return render_template("user_form.html", user=user, roles=roles)
        if not user['password']:
            flash("Пароль не может быть пустым", category="danger")
            return render_template("user_form.html", user=user, roles=roles)
        forbidden_chars = "~!@#$%^&*_-+()[]{}><\/|\"\'.,:;"
        if any(char in forbidden_chars for char in user['password']):
            flash("Пароль не должен содержать запрещенные символы", category="danger")
            return render_template("user_form.html", user=user, roles=roles)

        elif bool(re.search(r"\s", user['password'] ))==True:
            flash("Пароль не должен содержать пробелов", category="danger")
            return render_template("user_form.html", user=user, roles=roles)
        if len(user['login']) < 5:
            flash("Логин должен содержать не менее 5 символов", category="danger")
            return render_template("user_form.html", user=user, roles=roles)
        
        if len(user['password']) < 8 or len(user['password']) > 128:
            flash("Пароль должен содержать от 8 до 128 символов", category="danger")
            return render_template("user_form.html", user=user, roles=roles)
        
        if not any(c.isupper() for c in user['password']) or not any(c.islower() for c in user['password']):
            flash("Пароль должен содержать как минимум одну заглавную и одну строчную букву", category="danger")
            return render_template("user_form.html", user=user, roles=roles)
        
        if not any(c.isdigit() for c in user['password']):
            flash("Пароль должен содержать как минимум одну цифру", category="danger")
            return render_template("user_form.html", user=user, roles=roles)

        try:
            with db_connector.connect().cursor(named_tuple=True) as cursor:
                cursor.execute(query, user)
                db_connector.connect().commit()
            return redirect(url_for('users'))
        except DatabaseError as error:
            flash(f'Ошибка создания пользователя! {error}', category="danger")    
            db_connector.connect().rollback()

    return render_template("user_form.html", user=user, roles=roles)


@app.route('/user/<int:user_id>/change', methods=["GET", "POST"])
@login_required
def change_password(user_id):
    if request.method == 'POST':
        user = get_form_data(CHANGE_PASS_FIELDS)
        
        query_check_password = "SELECT user_id FROM users WHERE user_id = %s AND password = SHA2(%s, 256)"
        with db_connector.connect().cursor(named_tuple=True) as cursor:
            cursor.execute(query_check_password, (user_id, user["password"]))
            if not cursor.fetchone():
                flash("Текущий пароль введен неверно", category="danger")
                return redirect(url_for('change_password', user_id=user_id))
        
        if user["newpass"] == user["newpass2"]:
            forbidden_chars = "~!@#$%^&*_-+()[]{}><\/|\"\'.,:;"
            if any(char in forbidden_chars for char in user['newpass2']):
                flash("Пароль не должен содержать запрещенные символы", category="danger")
                return render_template("change.html")
            if len(user['newpass2']) < 8 or len(user['newpass2']) > 128:
                flash("Пароль должен содержать от 8 до 128 символов", category="danger")
                return render_template("change.html")
            if not user['newpass2']:
                flash("Пароль не может быть пустым", category="danger")
                return render_template("change.html", user=user)
            elif bool(re.search(r"\s", user['newpass2'] ))==True:
                flash("Пароль не должен содержать пробелов", category="danger")
            if not any(c.isupper() for c in user['newpass2']) or not any(c.islower() for c in user['newpass2']):
                flash("Пароль должен содержать как минимум одну заглавную и одну строчную букву", category="danger")
                return render_template("change.html")
        
            if not any(c.isdigit() for c in user['newpass2']):
                flash("Пароль должен содержать как минимум одну цифру", category="danger")
                return render_template("change.html")

            query_change_password = "UPDATE users SET password = SHA2(%s, 256) WHERE user_id = %s"
            try:
                with db_connector.connect().cursor(named_tuple=True) as cursor:
                    cursor.execute(query_change_password, (user["newpass"], user_id))
                    db_connector.connect().commit()
                    flash("Пароль успешно изменен", category="success")
                    return redirect(url_for('users'))
            except DatabaseError as error:
                flash(f'Ошибка изменения пароля! {error}', category="danger")
                db_connector.connect().rollback()
                return redirect(url_for('users'))
        else:
            flash("Новые пароли не совпадают", category="danger")
            return redirect(url_for('change_password', user_id=user_id))

    return render_template("change.html")




@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/secret')
@login_required
def secret():
    return render_template('secret.html')

# python -m venv ve
# . ve/bin/activate -- Linux
# ve\Scripts\activate -- Windows
# pip install flask python-dotenv