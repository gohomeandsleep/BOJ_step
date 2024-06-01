class olympic:
    def __init__(self, name, gold, silver, bronze, score):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
        self.score = score

n, k = map(int, input().split())

lst = []
for i in range(n):
    name, gold, silver, bronze = map(int, input().split())
    score = 1000000 * gold + 1000 * silver + bronze
    if name == k:
        country = i
        #print(i)
    lst.append(olympic(name, gold, silver, bronze, score))
    
country_id = lst[country]


rank = 1
for i in range(n):
    if lst[i].score > country_id.score:
        rank += 1

print(rank)