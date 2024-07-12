n, m = map(int, input().split())
lst = list(map(int, input().split()))
prefix = [0] * (len(lst) + 1)
prefix[1] = lst[0]
for i in range(2, len(lst) + 1):
    prefix[i] = lst[i-1] + prefix[i-1]
#print(prefix)

res = float('-inf')
for i in range(n-m+1):
    tmp = prefix[i+m] - prefix[i]
    if res < tmp:
        res = tmp

print(res)