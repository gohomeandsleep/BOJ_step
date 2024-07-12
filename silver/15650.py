import itertools

n, m = map(int, input().split())
lst = [i+1 for i in range(n)]
combs = itertools.combinations(lst, m)
for comb in combs:
    print(*comb, sep=' ')
