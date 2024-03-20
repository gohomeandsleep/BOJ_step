import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int, input().split())
arrx = []
arry = []
for i in range(1999):
  for j in range(1999):
    if a * (i-999) + b * (j-999) == c:
      arrx.append(i-999)
      arry.append(j-999)

ans = 0
i = 0
while ans == 0:
  if d * arrx[i] + e * arry[i] == f:
    print(arrx[i], arry[i])
    ans = 1
  i = i + 1