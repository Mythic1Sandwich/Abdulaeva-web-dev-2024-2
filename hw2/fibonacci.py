def fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        x = fib_list[i-1] + fib_list[i-2]
        fib_list.append(x ** 3)  # Возводим число в куб перед добавлением в список
    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))