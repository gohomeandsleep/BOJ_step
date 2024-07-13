n = int(input())
lst = list(map(int, input().split()))
lst.sort()

left, right = 0, n-1
res = [float('-inf'), 0]
dist = abs(sum(res))
while left < right:
    cur = lst[left] + lst[right]
    if cur == 0:
        res = [lst[left], lst[right]]
        break
    elif cur > 0:
        if abs(cur) < dist:
            res = [lst[left], lst[right]]
            dist = abs(sum(res))
        right -= 1
    else:
        if abs(cur) < dist:
            res = [lst[left], lst[right]]
            dist = abs(sum(res))
        left += 1

print(*res, sep=' ')