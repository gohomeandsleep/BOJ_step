T = int(input())
for _ in range(T):
    n = int(input())
    lst1 = list(map(int, input().split()))
    check = set(lst1)
    m = int(input())
    lst2 = list(map(int, input().split()))
    for num in lst2:
        if num in check:
            print(1)
        else:
            print(0)