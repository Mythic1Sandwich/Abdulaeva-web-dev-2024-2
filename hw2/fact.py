import time

def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n-1)

def fact_it(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
if __name__ == '__main__':
    a = int(input())
    start_time = time.time()
    print(fact_rec(a))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print(fact_it(a))
    print("--- %s seconds ---" % (time.time() - start_time))
# Вывод:
# Рекурсивная функция работает медленнее итерационной функции из-за большого количества вызовов функции
# Время выполнения итерационной функции намного быстрее времени выполнения рекурсивной функции
