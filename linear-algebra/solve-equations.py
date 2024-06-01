import numpy as np

# Find solution when equations having unique solutions
# 4x1 - 3x2 + x3 = -10
# 2x1 + x2 + 3x3 = 0
# -x1 + 2x2 - 5x3 = 17

A = np.array([
    [4, -3, 1],
    [2, 1, 3],
    [-1, 2, -5]],
    dtype=np.dtype(float))

b= np.array([-10, 0, 17], dtype=np.dtype(float))

print("Matrix A:")
print(A)
print("\nArray b")
print(b)

print(f"Shape of A:{np.shape(A)}")
print(f"Shape of b:{np.shape(b)}")

# Solve Equations
x = np.linalg.solve(A, b)
print(f"Solution: {x}")

# Find determinant
d = np.linalg.det(A)
print(f"Determinant of matrix a: {d:.2f}")

# Find solution when equations not having unique solutions
# x1 + x2 + x3 = 2
# x2 -3x3 = 1
# 2x1 + x2 + 5x3 = 0

A_2 = np.array([
    [1, 1, 1],
    [0, 1, -3],
    [2, 1, 5]],
    dtype=np.dtype(float))

b_2 = np.array([2, 1, 0], dtype=np.dtype(float))

print(np.linalg.solve(A_2, b_2))

d_2 = np.linalg.det(A_2)
print(f"Determinant of matrix A_2: {d_2:.2f}")