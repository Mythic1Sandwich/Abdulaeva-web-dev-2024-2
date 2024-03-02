def format_phone_number(phone_number):
    phone_number = ''.join(filter(str.isdigit, phone_number.strip()))

    if phone_number.startswith('8'):
        phone_number = '7' + phone_number[1:]

    
    formatted_number = '+7 ({}) {}-{}-{}'.format(phone_number[1:4], phone_number[4:7], phone_number[7:9], phone_number[9:])
    return formatted_number
if __name__ == '__main__':
    n = int(input())
    phone_numbers = [input() for i in range(n)]
    phone_numbers.sort()

    for number in phone_numbers:
        formatted = format_phone_number(number)
        print(formatted)
