
import csv
def price_sum():
    adult_sum = 0
    pensioner_sum = 0
    child_sum = 0

    with open('C:/Users/zarin/OneDrive/Рабочий стол/pythondev/hw1/products.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # пропустить заголовок файла
        for row in reader:
            adult_sum += float(row[1])
            pensioner_sum += float(row[2])
            child_sum += float(row[3])

    print('%.2f %.2f %.2f' % (adult_sum, pensioner_sum, child_sum))
price_sum()
