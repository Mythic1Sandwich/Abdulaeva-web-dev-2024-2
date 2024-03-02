def show(name, salary):

    if salary:
        return name + ": " + salary + " R"
    else:
        return name + ": " + '1000000' + " R"
if __name__ == '__main__':
    employee_name = input()
    employee_salary = input()
