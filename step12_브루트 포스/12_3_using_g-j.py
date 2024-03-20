numlist = list(map(int, input().split()))

A = [[numlist[0], numlist[1]], [numlist[3], numlist[4]]]
B = [numlist[2], numlist[5]]

# Perform Gaussian elimination
n = len(A)

for i in range(n):
    # Find the maximum element in the column below the current element
    max_row = i
    for j in range(i+1, n):
        if abs(A[j][i]) > abs(A[max_row][i]):
            max_row = j
            
    # Swap the maximum row with the current row
    A[i], A[max_row] = A[max_row], A[i]
    B[i], B[max_row] = B[max_row], B[i]
    
    # Make all the elements below the current element in the column zero
    for j in range(i+1, n):
        factor = A[j][i] / A[i][i]
        for k in range(i, n):
            A[j][k] -= factor * A[i][k]
        B[j] -= factor * B[i]

# Perform back substitution
X = [0] * n

for i in range(n-1, -1, -1):
    X[i] = B[i] / A[i][i]
    for j in range(i):
        B[j] -= A[j][i] * X[i]

print(round(X[0]), round(X[1]))