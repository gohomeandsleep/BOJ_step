n = int(input())
k = len(str(n))

asc = [i+1 for i in range(k)]
lst = [9*10 ** (i) for i in range(k-1)]
lst.append(n - 10 ** (k-1) + 1)

res = 0
for i in range(k):
    res += asc[i] * lst[i]
print(res)