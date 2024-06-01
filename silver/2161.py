n = int(input())

lst = [i+1 for i in range(n)]

for i in range(n):
    print(lst[0], end=' ')
    lst.pop(0)
    if len(lst) ==0:
        break
    else:
        k = lst[0]
        lst.append(k)
        lst = lst[1:]