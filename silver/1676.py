def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())

k = 1
for i in range(n):
    k = k * (n-i)

cnt = 0
end = False
check = -1

str_k = str(k)
digits = [int(digit) for digit in str_k]
#print(digits)
while end == False:
    #print(str_k[check])
    if str_k[check] != '0':
        end = True
    else:
        cnt += 1
        check -= 1
    
print(cnt)