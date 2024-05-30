n, k = map(int, input().split())
lst = [i+1 for i in range(n)]
cnt = 0
print("<", end='')
while len(lst) > 0:
    cnt = (cnt + k - 1) % len(lst) 
    if len(lst) == 1:
        print(lst.pop(cnt), end='>')
    else:
        print(lst.pop(cnt), end=', ')