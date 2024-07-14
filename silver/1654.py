k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]

left = 1
right = max(lst)
result = 0

while left <= right:
    mid = (left + right) // 2
    tmp = sum(i // mid for i in lst)
    
    if tmp >= n:
        result = mid
        left = mid + 1
    else:  
        right = mid - 1

print(result)