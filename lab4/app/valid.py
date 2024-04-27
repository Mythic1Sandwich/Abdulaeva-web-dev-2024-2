import re

def validate_login(login):
    if not login or len(login) < 5:
        return False
    if not re.match("^[a-zA-Z0-9]+$", login):
        return False
    return True

def validate_password(password):
    if not password or len(password) < 8 or len(password) > 128:
        return "Пароль должен быть длиной от 8 до 128 символов"
    if not re.match("^(?=.[a-z])(?=.[A-Z])(?=.*\d)[a-zA-Z\d]+$", password):
        return "Пароль должен содержать хотя бы одну строчную букву, одну заглавную букву и одну цифру"
    if re.search("\s", password):
        return "Пароль не должен содержать пробелы"
    return True

def validate_name(name):
    if not name:
        return False
    return True

def validate_surname(surname):
    if not surname:
        return False
    return True