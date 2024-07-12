n, dif = map(int, input().split())
lst = list(map(int, input().split()))

dist = 10000
for i in range(n):
    for j in range(i+1, n):
        #print(lst[i], lst[j])
        if abs(lst[i] - lst[j]) <= dif:
            if abs(i - j) < dist:
                dist = abs(i - j)

print(dist)