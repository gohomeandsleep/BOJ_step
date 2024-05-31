n = list(input())

#print(n)

word_lst = [0 for _ in range(9)]

for i in range(len(n)):
    if n[i] == '0':
        word_lst[0] += 1
    if n[i] == '1':
        word_lst[1] += 1
    if n[i] == '2':
        word_lst[2] += 1
    if n[i] == '3':
        word_lst[3] += 1
    if n[i] == '4':
        word_lst[4] += 1
    if n[i] == '5':
        word_lst[5] += 1
    if n[i] == '6' or n[i] == '9':
        word_lst[6] += 1
    if n[i] == '7':
        word_lst[7] += 1
    if n[i] == '8':
        word_lst[8] += 1

if word_lst[6] % 2 == 0:
    word_lst[6] = word_lst[6] // 2
else:
    word_lst[6] = word_lst[6] // 2 + 1

print(max(word_lst))