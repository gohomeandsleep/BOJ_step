n = int(input())

res = 0
if n == 1 or n == 3:
    res = -1
elif n % 5 == 0:
    res = n // 5
elif n % 2 == 0:
    res = (n - n % 10) // 5 + (n % 10) // 2
elif n % 10 < 5:
    #print((n // 5 - 1),(n % 5 + 5) // 2 )
    res = (n // 5 - 1) + (n % 5 + 5) // 2
elif n % 10 > 5:
    #print(n // 5,(n - 5 * (n // 5)) // 2 )
    res = n // 5 + (n - 5 * (n // 5)) // 2


print(res)