from collections import deque
def query(inst, lst):
    queue = deque(lst)
    reverse_flag = False
    for i in inst:
        #print(queue)
        if i == 'R':
            reverse_flag = not reverse_flag
        elif i == 'D':
            if len(queue) > 0:
                if reverse_flag:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                return 'error'
            
    res = list(queue)
    if reverse_flag:
        res.reverse()
    return res


T = int(input())
for _ in range(T):
    inst = list(input())
    n = int(input())
    lst = eval(input())

    res = query(inst, lst)
    if res == 'error':
        print('error')
    else:
        print('[', end='')
        print(*res, sep=',', end='')
        print(']')