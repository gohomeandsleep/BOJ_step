import sys

n = int(input())
lamp = list(map(int, input().split()))
#print(lamp)
m = int(input())
std = []
for i in range(m):
    std.append(sys.stdin.readline().split())

for i in range(m):
    if std[i][0] == '1':
        k = int(std[i][1])
        for j in range(k-1, n, k):
            if lamp[j] == 1:
                lamp[j] = 0
            else:
                lamp[j] = 1
        #print(lamp)
    else:
        stp = int(std[i][1]) -1
        endp = int(std[i][1]) -1
        
        while stp > 0 and endp < n-1 and lamp[stp-1] == lamp[endp+1]:
            stp -= 1
            endp += 1
        
        for i in range(stp, endp+1):
            if lamp[i] == 1:
                lamp[i] = 0
            else:
                lamp[i] = 1
        #print(lamp)

for i in range((n-1) // 20 + 1):
    print(*lamp[20*i:20*(i+1)], sep=' ')
    