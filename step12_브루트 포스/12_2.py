n = int(input())

ans = 0
for i in range(1, n+1):
    #배열에 각 자리 수를 저장해 더해서 n과 같은지 확인
    a = []
    for digit in str(i):
        a.append(int(digit))
    #가장 작은 ans를 찾으므로 ans가 0일때만 값 변경
    if i + sum(a) == n and ans == 0:
        ans = i
        break

print(ans)