n = int(input())
lst = list(map(int, input().split()))
k = int(input())

cnt = 0
lst.sort()
cnt = 0
left, right = 0, n - 1

while left < right:
    current_sum = lst[left] + lst[right]
    if current_sum == k:
        cnt += 1
        left += 1
        right -= 1
    elif current_sum < k:
        left += 1
    else:
        right -= 1

print(cnt)