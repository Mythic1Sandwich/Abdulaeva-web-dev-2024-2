def python_if_else():
    n = int(input())
    if n<=100:
        if n%2 == 0:
            if 2<=n<=5:
                print('Not Weird')
            elif 6<=n<=20:
                print('Weird')
            elif n>20:
                print('Not Weird')
        else:
            print('Weird')
    else:
        print('Inacceptable')
python_if_else()