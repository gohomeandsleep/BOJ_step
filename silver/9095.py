def func(n):
    if n == 1:
        return 1
    lst = [1] * (n+1)
    lst[2] = 2
    for i in range(3, n+1):
        lst[i] = lst[i-1] + lst[i-2] + lst[i-3]
    return lst[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(func(n))