import re

def validate(phone_number):
    pattern = r'^(\+7|8|\+)?[\s\(\)\-\.\+\d]+$'
    
    if not re.match(pattern, phone_number):
        return 'Недопустимый ввод. В номере телефона встречаются недопустимые символы.'
    
    phone_number = re.sub(r'\D', '', phone_number) 
    if (len(phone_number) != 11  and len(phone_number) != 10) or (len(phone_number) == 11 and not(phone_number.startswith('8') or phone_number.startswith('7')) ):
        return 'Недопустимый ввод. Неверное количество цифр.'
    return ""
def formats(phone_number):
    phone_number = re.sub(r'\D', '', phone_number) 
    if len(phone_number) == 11 and (phone_number.startswith('8') or phone_number.startswith('7')) :
        phone_number = phone_number[1:]
    formatted_number = f'8-{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:8]}-{phone_number[8:]}'
    return formatted_number
