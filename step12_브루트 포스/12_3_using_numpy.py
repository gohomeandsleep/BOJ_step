import numpy as np

numlist = list(map(int, input().split()))

#1행부터 차례로 작성
A = np.array([[numlist[0], numlist[1]], [numlist[3], numlist[4]]])
#상수 행렬 작성
B = np.array([numlist[2], numlist[5]])

# 연립일차식 풀이
X = np.linalg.solve(A, B)
#리스트 형태로 바꾸어서 표현
X = X.tolist()

print(round(X[0]), round(X[1]))