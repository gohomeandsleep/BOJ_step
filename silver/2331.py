def digit_power_sum(n, m):
    tmp_res = 0
    while n > 0:
        tmp_res += (n % 10) ** m
        n //= 10
    return tmp_res 

n, m = map(int, input().split())
lst = [n]

while True:
    n = digit_power_sum(n, m)
    if n not in lst:
        lst.append(n)
    else:
        k = lst.index(n)
        lst = lst[:k]
        break

print(len(lst))