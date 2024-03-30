def phonecheck(phonenumber: str) -> str:
    
    for char in '()-.+ ':
        phonenumber = phonenumber.replace(char, "")

    if not phonenumber.isdigit():
        return "Недопустимый ввод. В номере телефона встречаются недопустимые символы!"

    if not (10 <= len(phonenumber) <= 11):
        return "Недопустимый ввод. Неверное количество цифр!"

    return ""

def formatphone(phonenumber: str) -> str:
    
    phonenumber = ''.join(filter(str.isdigit, phonenumber))
    
    if phonenumber.startswith("8"):
        phonenumber = phonenumber[1:]

    elif phonenumber.startswith("7"):
        phonenumber = phonenumber[1:]

    return f"8-{phonenumber[:3]}-{phonenumber[3:6]}-{phonenumber[6:8]}-{phonenumber[8:10]}"