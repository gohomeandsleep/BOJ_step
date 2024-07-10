line, brand = map(int, input().split())
bundle = []
single = []
for i in range(brand):
    a, b = map(int, input().split())
    bundle.append(a)
    single.append(b)

if min(single) * 6 <= min(bundle):
    print(line * min(single))
else:
    print(min(min(bundle) * (line // 6) + min(single) * (line % 6), min(bundle) * (line // 6 + 1)))