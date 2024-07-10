n = int(input())
m = int(input())
lst = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(i+1, n):
        if lst[i] + lst[j] == m:
            res += 1

print(res)