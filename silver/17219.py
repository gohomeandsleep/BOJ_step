import sys

n, m = map(int, input().split())

urls = []
pws = []
for i in range(n):
    url, pw = sys.stdin.readline().split()
    urls.append(url)
    pws.append(pw)
target = [sys.stdin.readline().rstrip() for _ in range(m)]

for i in range(m):
    res = urls.index(target[i])
    print(pws[res])