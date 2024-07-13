T = int(input())
for _ in range(T):
    n = int(input())
    lst1 = list(map(int, input().split()))
    lst = [[i+1, lst1[i]] for i in range(n)]

    cnt = 0
    visited = set()
    for i in range(n):
        #고리의 길이가 1인 경우
        if lst[i][0] == lst[i][1]:
            visited.add(lst[i][0])
            cnt += 1
        #고리의 길이가 1이 아닌 경우
        else:
            if lst[i][0] not in visited:
                current = lst[i][0]
                #visited을 갈 때까지 고리의 모든 요소-> visited
                while current not in visited:
                    visited.add(current)
                    next = lst[current-1][1]
                    current = next
                cnt += 1
    print(cnt)