
import random
import math

def circle_square_mk(r, n):
    count_inside = 0

    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)

        if math.sqrt(x**2 + y**2) <= r:
            count_inside += 1
    
    square_estimation = (2 * r)**2 * (count_inside / n)
    return square_estimation

if __name__ == '__main__':
    r = int(input())
    n = int(input())
    estimated_square = circle_square_mk(r, n)
    actual_square = math.pi * r**2

    print("Оценка площади:", estimated_square)
    print("Площадь по формуле:", actual_square)
    print("Погрешность:", abs(actual_square - estimated_square))

# погрешность расчета зависит от количества экспериментов 
# 
# Чем больше экспериментов 
# тем более точный результат мы получим.
# При увеличении значения n погрешность будет уменьшаться.