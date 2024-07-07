lst = list(input())

for i in range(len(lst)):
    lst[i] = int(lst[i])

if 0 in lst and sum(lst) % 3 == 0:
    lst.sort(reverse=True)
    for i in range(len(lst)):
        print(lst[i], end='')
else:
    print(-1)