n, m = map(int, input().split())

org_lst = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    sum = 0
    for i in range(y1-1, y2):
        for j in range(x1-1, x2):
            sum += org_lst[j][i]
    
    print(sum)