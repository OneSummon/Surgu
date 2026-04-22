import numpy as np

# Задание 1 способ 1
A = np.array([
    [1,  2, -1],
    [2, -3,  1],
    [1,  1, -1]
])
b = np.array([7, 3, 16])

x = np.linalg.solve(A, b)
print("Задание 1 способ 1")
print(x)
print()

# Задание 1 способ 2
A = np.array([
    [1,  2, -1],
    [2, -3,  1],
    [1,  1, -1]
], dtype=float)
b = np.array([7, 3, 16], dtype=float)

D = np.linalg.det(A)
x = np.zeros(3)
for i in range(3):
    Ai = A.copy()
    Ai[:, i] = b
    x[i] = np.linalg.det(Ai) / D

print("Задание 1 способ 2")
print(x)
print()


# Задание 2 способ 1
A = np.array([
  [1,1,1,1,1],
  [0,2,1,1,1],
  [0,0,3,1,1],
  [0,0,0,4,1],
  [0,0,0,0,5]
], dtype=float)
b = np.array([5,4,3,2,1],
             dtype=float)

x = np.linalg.solve(A, b)
print("Задание 2 способ 1")
print(x)
print()

# Задание 2 способ 2
A = np.array([
  [1,1,1,1,1],
  [0,2,1,1,1],
  [0,0,3,1,1],
  [0,0,0,4,1],
  [0,0,0,0,5]
], dtype=float)
b = np.array([5,4,3,2,1],
             dtype=float)
n = len(b)

# Обратный ход:
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = b[i]
    for j in range(i+1, n):
        x[i] -= A[i,j] * x[j]
    x[i] /= A[i,i]

print("Задание 2 способ 2")
print(x)
print()


# Задание 3 способ 1
A = np.array([
  [5,0,0,0,0],
  [1,5,0,0,0],
  [1,1,5,0,0],
  [1,1,1,5,0],
  [1,1,1,1,5]
], dtype=float)
b = np.ones(5)

x = np.linalg.solve(A, b)
print("Задание 3 способ 1")
print(x)
print()

# Задание 3 способ 2
n = 5
A = np.array([
  [5,0,0,0,0],
  [1,5,0,0,0],
  [1,1,5,0,0],
  [1,1,1,5,0],
  [1,1,1,1,5]
], dtype=float)
b = np.ones(n)

# Прямой ход Гаусса
for k in range(n):
    for i in range(k+1, n):
        f = A[i,k] / A[k,k]
        A[i,:] -= f * A[k,:]
        b[i] -= f * b[k]

# Обратный ход
x = np.zeros(n)
for i in range(n-1,-1,-1):
    x[i] = (b[i] - A[i,i+1:]
            @ x[i+1:]) / A[i,i]
    
print("Задание 3 способ 1")
print(x)