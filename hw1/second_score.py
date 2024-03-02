def second_score():
    n = int(input())
    A = list(map(int, input().split()))
    A = list(set(A))
    A.sort(reverse=True)

    result = str(A[1]) if len(A) > 1 else "No second highest score"
    print(result)
second_score()