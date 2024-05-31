import time

n = int(input())

res = 0
bl = True
while bl == True:
    tmp = res * (res+1) // 2
    if tmp > n:
        bl = False
    else:
        res += 1

print(res-1)