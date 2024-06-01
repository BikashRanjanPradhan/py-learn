import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [-1, 3],
    [3, 2]
], dtype= np.dtype(float))

b = np.array([7, 1], dtype=np.dtype(float))

print(f"Matrix A: \n {A}")
print(f"Array b: \n {b}")

# Dimension
print(f"Shape of A: {A.shape}")
print(f"Shape of b: {b.shape}")

print(f"Shape of A: {np.shape(A)}")
print(f"Shape of b: {np.shape(b)}")

# Solve two equaltions
x = np.linalg.solve(A, b)
print(f"Solution : {x}")

# Determinant
d= np.linalg.det(A)
print(f"Determinant of A: {d:.2f}")

# Reshape
A_system = np.hstack((A, b.reshape((2, 1))))
print(f"A_system: {A_system}")
print(f"A_system_1: {A_system[1]}")

# Plot line
plot_lines(A_system)

