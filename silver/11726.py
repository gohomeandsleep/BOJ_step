def fibo(n):
    fib = [1] * (n + 1)
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
n = int(input())
print(fibo(n) % 10007)