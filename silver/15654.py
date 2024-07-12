import itertools
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
combs = itertools.permutations(lst, m)
for comb in combs:
    print(*comb, sep=' ')