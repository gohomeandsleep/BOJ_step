lst = list(input())

lst01 = [0, 0]
k = int(lst[0])
lst01[k] += 1
for i in range(1, len(lst)):
    #print(lst[i])
    if lst[i] == '0':
        if lst[i-1] != '0':
            lst01[0] += 1
    else:
        if lst[i-1] != '1':
            lst01[1] += 1

print(min(lst01))