
def my_sum(*args):
    return sum(args)
if __name__ == '__main__':
    numbers = []
    while True:
        num = float(input())
        if num == 0:
            break
        numbers.append(num)

    print(my_sum(*numbers))
