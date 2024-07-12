comp = int(input())
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

res = set([1])
for _ in range(n):
    for i in range(n):
        if lst[i][0] in res:
            res.add(lst[i][1])
        elif lst[i][1] in res:
            res.add(lst[i][0])

print(len(res)-1)