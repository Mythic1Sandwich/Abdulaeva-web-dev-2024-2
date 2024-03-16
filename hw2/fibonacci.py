cube = lambda x: x**3

def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        next = fib[-1] + fib[-2]
        fib.append(next)
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
