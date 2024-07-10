n = int(input())
lst = {}
for _ in range(n):
    k = int(input())
    if k not in lst:
        lst[k] = 1
    else:
        lst[k] += 1

max_freq = max(lst.values())
min_value_with_max_freq = min(key for key, value in lst.items() if value == max_freq)
print(min_value_with_max_freq)