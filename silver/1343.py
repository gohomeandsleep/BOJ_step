lst = list(input())
cnt = 0
cnt_lst = []
if lst[0] == '.':
    cnt_lst.append(0)
else:
    cnt += 1
for i in range(1, len(lst)):
    if lst[i] == 'X':
        cnt += 1
    if lst[i] == '.':
        if lst[i-1] != '.':
            cnt_lst.append(cnt)
            cnt = 0
        cnt_lst.append(cnt)

if cnt >0:
    cnt_lst.append(cnt)

a = 'AAAA'
b = 'BB'

print(cnt_lst)

bl = True

if cnt_lst == []:
    bl = False

for i in range(len(cnt_lst)):
    if cnt_lst[i] %2 == 1:
        bl = False

if bl == True:
    for i in range(len(cnt_lst)):
        if cnt_lst[i] == 0:
            print(".", end='')
        else:
            if cnt_lst[i] % 4 == 0:
                for k in range(cnt_lst[i] // 4):
                    print(a, end='')
            else:
                for k in range(cnt_lst[i] // 4):
                    print(a, end='')
                print(b, end='')
else:
    print(-1)