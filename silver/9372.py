T = int(input())

for _ in range(T):
    city, plane = map(int, input().split())
    lst = [input().split() for _ in range(plane)]
    print(city - 1)