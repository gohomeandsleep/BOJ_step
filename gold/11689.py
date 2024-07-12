n = int(input())
while n != 0:
    k = n
    lst = set()
    if n == 1:
        k = 0
    while n % 2 == 0:
        lst.add(2)
        n //= 2
    for i in range(3, int(n ** 0.5)+1, 2):
        while n % i == 0:
            lst.add(i)
            n //= i

    if n > 2:
        lst.add(n)

    lst = list(lst)
    #print(lst)

    for i in lst:
        k = k * (i-1) // i

    print(k)
    n = int(input())
