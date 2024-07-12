def func(n):
    lst = [1] * (101)
    lst[3] = 2
    lst[4] = 2
    lst[5] = 3
    lst[6] = 4
    lst[7] = 5
    lst[8] = 7
    for i in range(9, n+1):
        lst[i] = lst[i-1] + lst[i-5]
    return lst[n-1]

T = int(input())
for _ in range(T):
    n = int(input())
    print(func(n))