from sympy import symbols, Eq, solve

# Define the variables
x, y = symbols('x y')

numlist = list(map(int, input().split()))

# Define the equations
equation1 = Eq(numlist[0]*x + numlist[1]*y, numlist[2])
equation2 = Eq(numlist[3]*x + numlist[4]*y, numlist[5])

# Solve the equations
solution = solve((equation1, equation2), (x, y))

for key, value in solution.items():
    print(value, end=" ")