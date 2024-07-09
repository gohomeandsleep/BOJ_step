n, m = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
for i in range(n):
    #print(lst)
    sum = lst[0]
    k = 1
    if lst[0] == m:
        res += 1
    while sum <= m and i+k < n:
        sum += lst[k]
        #print(sum)
        k += 1
        if sum == m:
            res += 1
            #print("ok")
    lst = lst[1:]

print(res)