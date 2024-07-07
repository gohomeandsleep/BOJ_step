n, k = map(int, input().split())

lst = [int(input()) for _ in range (n)]

lst.sort(reverse=True)

res = 0
for ind in lst:
    if k // ind != 0:
        res += k // ind
        k -= (k // ind) * ind

print(res)