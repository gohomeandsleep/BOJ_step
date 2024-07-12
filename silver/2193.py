def fibo(n):
    lst = [1] * 91
    for i in range(2, n+1):
        lst[i] = lst[i-1] + lst[i-2]
    return lst[n-1]

n = int(input())
print(fibo(n))