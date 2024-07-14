T = int(input())
for _ in range(T):
    n = int(input())
    lst = {}
    for _ in range(n):  
        name, style = input().split()
        if style not in lst:
            lst[style] = 2
        else:
            lst[style] += 1
    res = list(lst.values())
    p = 1
    for i in range(len(res)):
        p *= res[i]
    print(p - 1)