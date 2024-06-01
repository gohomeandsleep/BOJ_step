a1 = 1
a2 = 1

n = int(input())
for i in range(n-1):
    temp = a2
    a2 = a1 + a2
    a1 = temp
    #print(a1, a2)

if n == 1:
    print('4')
else:
    print(a2 * 2 + a1 * 2)