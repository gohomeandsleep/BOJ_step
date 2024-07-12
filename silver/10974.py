import itertools

n = int(input())
lst = [i+1 for i in range(n)]
combs = itertools.permutations(lst, n)

for comb in combs:
    print(*comb, sep=' ')