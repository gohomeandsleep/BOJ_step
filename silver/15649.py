import itertools

n, m = map(int, input().split())
items = [i+1 for i in range(n)]
perms = itertools.permutations(items, m)

for perm in perms:
    print(*perm, sep=' ')