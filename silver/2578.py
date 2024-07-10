def bingo_check(lst):
    cnt = 0
    for i in range(5):
        if lst[5*i] == 1 and lst[5*i+1] == 1 and lst[5*i+2] == 1 and lst[5*i+3] == 1 and lst[5*i+4] == 1:
            cnt += 1
        if lst[i] == 1 and lst[5+i] == 1 and lst[10+i] == 1 and lst[15+i] == 1 and lst[20+i] == 1:
            cnt += 1
    if lst[0] == 1 and  lst[6] == 1 and lst[12] == 1 and lst[18] == 1 and lst[24] == 1:
        cnt += 1
    if lst[4] == 1 and lst[8] == 1 and lst[12] == 1 and lst[16] == 1 and lst[20] == 1:
        cnt += 1
    return cnt    

callee = []
for _ in range(5):
    lst = list(map(int, input().split()))
    callee = callee + lst
caller = []
for _ in range(5):
    lst = list(map(int, input().split()))
    caller = caller + lst

bingo_board = [0 for _ in range(25)]
for i in range(25):
    k = callee.index(caller[i])
    bingo_board[k] = 1
    if bingo_check(bingo_board) >= 3:
        print(i+1)
        break