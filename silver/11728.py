n, m = map(int, input().split())

lst_n = list(map(int, input().split()))
lst_m = list(map(int, input().split()))

lst = lst_n + lst_m
lst.sort()

print(*lst)