n = int(input())

lst = list(map(int, input().split()))
res = []

for value in lst:
    if value not in res:
        res.append(value)

res.sort()

print(*res)