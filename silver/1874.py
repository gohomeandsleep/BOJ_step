n = int(input())
inst = [int(input()) for _ in range(n)]
lst = [i+1 for i in range(n)]

stack = []
stat = True
res = []
for i in range (n):
    if len(stack) > 0 and stack[-1] == inst[i]:
        stack.pop(-1)
        res.append('-')
    elif len(lst) > 0 and inst[i] >= lst[0]:
        while len(lst) > 0 and inst[i] >= lst[0]:
            stack.append(lst.pop(0))
            res.append('+')
        stack.pop(-1)
        res.append('-')
    else:
        stat = False

if stat == False:
    print('NO')
else:
    print(*res, sep='\n')