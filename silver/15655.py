import itertools
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
combs = itertools.combinations(lst, m)
for comb in combs:
    print(*comb, sep=' ')