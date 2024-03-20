from itertools import combinations
from math import comb

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

temp_list = list(combinations(num_list, 3))

max_sum = 0
for combination in temp_list:
    part_sum = sum(combination)
    if part_sum >= max_sum and part_sum <= m:
        max_sum = part_sum

print(max_sum)