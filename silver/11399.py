n = int(input())
lst = list(map(int, input().split()))

lst.sort()

res = 0
for i in range(n):
    res += sum(lst[:i+1])
    #print(lst[:i+1])

print(res)