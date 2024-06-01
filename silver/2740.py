n1, m1 = map(int, input().split())
lst_a = [list(map(int, input().split())) for _ in range(n1)]

n2, m2 = map(int, input().split())
lst_b = [list(map(int, input().split())) for _ in range(n2)]

lst = [[0 for _ in range(m2)] for _ in range(n1)]

for i in range(n1):
    for j in range(m2):
        sum = 0
        for k in range(m1):
            sum += lst_a[i][k] * lst_b[k][j]
        lst[i][j] = sum

for i in range(n1):
    print(*lst[i])