import numpy as np

numlist = list(map(int, input().split()))

# Define the coefficients matrix (A) and the constants vector (B)
A = np.array([[numlist[0], numlist[1]], [numlist[3], numlist[4]]])
B = np.array([numlist[2], numlist[5]])

# Solve the system of linear equations
X = np.linalg.solve(A, B)

X = X.tolist()

print(round(X[0]), round(X[1]))