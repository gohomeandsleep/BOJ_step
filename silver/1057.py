def calculate_route(node, height):
    route = []
    for i in range(height, 0, -1):
        if node > lst[i-1]:
            node -= lst[i-1]
            route.append(1)
        else:
            route.append(0)
    return route

n, a, b = map(int, input().split())
lst = [2 ** i for i in range (17)]

#depth finder
h = 17
for i in range(16):
    #print(n, n // lst[i], n // lst[i+1])
    if (n-1) // lst[i] == 1 and (n-1) // lst[i+1] == 0:
        h = i + 1
#print(h)

a_route = calculate_route(a, h)
b_route = calculate_route(b, h)
#print(a_route)
#print(b_route)

cnt = h
for i in range(h):
    if a_route[i] == b_route[i]:
        cnt -= 1
    else:
        break

print(cnt)