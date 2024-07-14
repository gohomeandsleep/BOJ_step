n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

res = dist[0] * price[0]
lowest = price[0]
for i in range(1, len(dist)):
    if lowest > price[i]:
        lowest = price[i]
    res += lowest * dist[i]

print(res)