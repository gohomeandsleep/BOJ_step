def fibo(n):
    lst0 = [1] * 41
    lst1 = [1] * 41
    lst0[1] = 0
    lst1[0] = 0
    for i in range(2, n+1):
        lst0[i] = lst0[i-1] + lst0[i-2]
        lst1[i] = lst1[i-1] + lst1[i-2]
    return [lst0[n], lst1[n]]

T = int(input())
for _ in range(T):
    n = int(input())
    print(*fibo(n), sep=' ')