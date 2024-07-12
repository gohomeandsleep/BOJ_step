def cal(n):
    lst = [1] * (n + 1)
    for i in range(2, n + 1):
        lst[i] = 2 * lst[i-2] + lst[i-1]
    return lst[n]
n = int(input())
print(cal(n) % 10007)