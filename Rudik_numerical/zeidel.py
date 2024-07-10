import numpy as np

def gauss_seidel(A, b, x0, epsilon, max_iterations):
    n = len(A)
    x = x0.copy()

    #Gauss-Seidal Method [By Bottom Science]

    for i in range(max_iterations):
        x_new = np.zeros(n)
        for j in range(n):
            s1 = np.dot(A[j, :j], x_new[:j])
            s2 = np.dot(A[j, j + 1:], x[j + 1:])
            x_new[j] = (b[j] - s1 - s2) / A[j, j]
        if np.allclose(x, x_new, rtol=epsilon):
            return x_new
        x = x_new
    return x

A = np.array([[10.1, -1.1, 2, 0.1],
              [-1, 11, -12, 3],
              [2, -1, 11, -1],
              [0, 3, -1, 8]])
b = np.array([6, 25, -11, 15])
x0 = np.zeros(4)
eps = 1e-5
max_iter = 100

x = gauss_seidel(A, b, x0, eps, max_iter)
print(x)

A = np.array([[12, -1, 2, 0],
              [-12, 11, -12, 3],
              [4, -3, 11, -1],
              [0, 1, -1, 8]])
b = np.array([1, 20, -11, 15])
x0 = np.zeros(4)
eps = 1e-5
max_iter = 100

x = gauss_seidel(A, b, x0, eps, max_iter)
print(x)