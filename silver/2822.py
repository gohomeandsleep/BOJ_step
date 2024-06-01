class score:
    def __init__(self, sc, num):
        self.sc = sc
        self.num = num
    
lst = []
for i in range(8):
    k = int(input())
    lst.append(score(k, i+1))

lst.sort(key=lambda x:x.sc, reverse=True)

lst = lst[:5]

lst.sort(key=lambda x:x.num)

print(sum(score.sc for score in lst))
for score in lst:
    print((score.num), end=' ')