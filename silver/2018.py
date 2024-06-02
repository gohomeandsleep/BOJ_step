n = int(input())
lst = [i+1 for i in range(n)]

cnt = 0
do = 0
for i in range(n): #시작점
    current_sum = 0
    for j in range(i, n): #개수
        current_sum += lst[j]
        do += 1
        if current_sum == n:
            cnt += 1
            #print(lst[i:j+1])
        elif current_sum > n:
            break

print(cnt, do)