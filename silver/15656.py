import itertools
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
combs = itertools.product(lst, repeat=m)
for comb in combs:
    print(*comb, sep=' ')