a, b = input().split()
a = list(a)
b = list(b)

min = 50
for i in range(len(b) - len(a) + 1):
    tmp = 0
    for j in range(len(a)):
        #print(a[j], b[i+j])
        if a[j] != b[i+j]:
            tmp += 1
    if tmp < min:
        min = tmp

print(min)