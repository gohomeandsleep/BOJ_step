n = int(input())
lst = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n-1, 0, -1):
    if lst[i-1] >= lst[i]:
        cnt += (lst[i-1] - lst[i] + 1)
        lst[i-1] -= (lst[i-1] - lst[i] + 1)

print(cnt)