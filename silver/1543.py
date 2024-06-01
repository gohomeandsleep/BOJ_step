lst = list(input())
sample = list(input())

cnt = 0
i = 0
while i <= (len(lst) - len(sample)):
    sum = 0
    for j in range(len(sample)):
        if lst[i+j] == sample[j]:
            sum += 1
    if sum == len(sample):
        cnt += 1
        i += len(sample)
    else:
        i += 1
print(cnt)