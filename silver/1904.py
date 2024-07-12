def func(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    lst = [1] * (n+1)
    lst[1] = 2
    for i in range(2, n + 1):
        lst[i] = lst[i-1] % 15746 + lst[i-2] % 15746 
    return lst[n-1] % 15746

n = int(input())
print(func(n))