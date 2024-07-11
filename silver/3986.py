N = int(input())
res = 0
for _ in range(N):
    lst = list(input())
    stack = []
    for j in range(len(lst)):
        if len(stack) == 0 or stack[-1] != lst[j]:
            stack.append(lst[j])
        elif stack[-1] == lst[j]:
            stack.pop(-1)
    if len(stack) == 0:
        res += 1
print(res)