import sys

n = int(input())
lst = []
cnt = []
for _  in range(n):
    book = sys.stdin.readline().rstrip()
    if book not in lst:
        lst.append(book)
        cnt.append(1)
    else:
        idx = lst.index(book)
        cnt[idx] += 1

mx = max(cnt)
res = []
for i in range(len(cnt)):
    if cnt[i] == mx:
        res.append(lst[i])

res.sort()
print(res[0])