def print_function():
    n = int(input())
    if 1<=n<=20:
        for i in range(1, n+1):
            print(i, end='')
        print()
    else:
        print('ERROR')
print_function()