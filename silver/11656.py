lst = list(input())

lsts = []
for i in range(len(lst)):
    lsts.append(lst[i:])

lsts.sort()

for i in range(len(lsts)):
    print(*lsts[i], sep = '')