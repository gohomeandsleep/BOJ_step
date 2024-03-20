from itertools import combinations
from math import comb

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
#세 숫자를 더하기 위해 조합 리스트 저장
temp_list = list(combinations(num_list, 3))
#모든 경우에 걸쳐서 가장 크면서 m을 넘지 않는 조합 찾기
max_sum = 0
for combination in temp_list:
    part_sum = sum(combination)
    if part_sum >= max_sum and part_sum <= m:
        max_sum = part_sum

print(max_sum)