import numpy as np


print("=" * 60)
print("ЗАДАНИЕ 1:  (A + 3B^T)(3A^T - B) X = C")
print("=" * 60)

A = np.array([[4, -1, 7],
              [0,  1, -2],
              [0,  0,  9]], dtype=float)

B = np.array([[-1, 1,  0],
              [ 0, 0,  3],
              [ 6, 2, -1]], dtype=float)

C = np.array([[5, 1, 1],
              [1, 5, 1],
              [1, 1, 5]], dtype=float)

M = (A + 3 * B.T) @ (3 * A.T - B)   # собираем левую матрицу

X1 = np.linalg.solve(M, C) + 0
print("X =\n", np.round(X1, 6))
print(f"Проверка ||MX - C|| = {np.linalg.norm(M @ X1 - C):.2e}\n")



print("=" * 60)
print("ЗАДАНИЕ 2:  (A²B + B³A)^T X = BC")
print("=" * 60)

A = np.array([[-1,  2, -4],
              [ 1, -1,  7],
              [-1,  0,  0]], dtype=float)

B = np.array([[1, 0, 0],
              [0, 2, 0],
              [1, 0, 3]], dtype=float)

C = np.array([[ 3,  8, -1],
              [ 0,  8,  0],
              [ 2, -1,  3]], dtype=float)

A2 = A @ A
B3 = B @ B @ B
M  = (A2 @ B + B3 @ A).T
BC = B @ C

X2 = np.linalg.solve(M, BC) + 0
print("X =\n", np.round(X2, 6))
print(f"Проверка ||MX - BC|| = {np.linalg.norm(M @ X2 - BC):.2e}\n")



print("=" * 60)
print("ЗАДАНИЕ 3:  (A³ - 2A² + 3A)^T X = 4B² - B")
print("=" * 60)

A = np.array([[2, -1, -1],
              [0,  2, -1],
              [0,  0, -1]], dtype=float)

B = np.array([[-1,  0,  0],
              [ 1, -3,  0],
              [ 1,  1, -5]], dtype=float)

A2 = A @ A
A3 = A2 @ A
B2 = B @ B
M = (A3 - 2 * A2 + 3 * A).T
after_equals = 4 * B2 - B

X3 = np.linalg.solve(M, after_equals) + 0
print("X =\n", np.round(X3, 6))
print(f"Проверка || MX - (4B²-B)|| = {np.linalg.norm(M @ X3 - after_equals):.2e}\n")