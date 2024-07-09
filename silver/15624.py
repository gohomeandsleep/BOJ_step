def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b % 1000000007, (a + b) % 1000000007
    return b

n = int(input())
print(fibonacci(n))
