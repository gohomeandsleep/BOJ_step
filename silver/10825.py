class Scores:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
lst = []
for _ in range(n):
    nam, k, e , m = input().split()
    lst.append(Scores(nam, int(k), int(e), int(m)))

lst.sort(key=lambda x: (-x.kor, x.eng, -x.math, x.name))

for i in range(n):
    print(lst[i].name)