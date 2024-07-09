def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
lst = list(map(int, input().split()))

for i in range(1, n):
    k = gcd(lst[0], lst[i])
    print("%d/%d" % (lst[0] // k, lst[i] // k))