n = int(input())
x1, y1, x2, y2 = map(int, input().split())

if x1 * n + y1 == x2 * n + y2:
    print("Yes", end=' ')
    print(x1 * n + y1)
else:
    print("No")