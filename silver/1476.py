earth, sun, moon = map(int, input().split())

pri_e = 1
pri_s = 1
pri_m = 1
stat = True
cnt = 1
while stat == True:
    if pri_e == earth and pri_s == sun and pri_m == moon:
        stat = False
    else:
        if pri_e == 15:
            pri_e -= 14
        else:
            pri_e += 1
        if pri_s == 28:
            pri_s -= 27
        else:
            pri_s += 1
        if pri_m == 19:
            pri_m -= 18
        else:
            pri_m += 1
        cnt += 1

print(cnt)