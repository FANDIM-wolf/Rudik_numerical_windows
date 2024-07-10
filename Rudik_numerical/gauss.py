import numpy as np

def solve_system_gauss_seidel(A, b, tol):
    """
    Решает систему линейных уравнений Ax = b методом Зейделя.
    
    Параметры:
    A (numpy.ndarray): Матрица коэффициентов системы линейных уравнений.
    b (numpy.ndarray): Вектор правых частей системы линейных уравнений.
    tol (float): Точность решения (по умолчанию 1e-5).
    
    Возвращает:
    numpy.ndarray: Решение системы линейных уравнений.
    int: Количество итераций, выполненных для достижения заданной точности.
    numpy.ndarray: Корни всех итераций.
    """
    
    # Расширенная матрица
    AB = np.hstack((A, b.reshape(-1, 1)))
    
    # Нормализация матрицы A
    for i in range(A.shape[0]):
        AB[i, :-1] /= 1
        AB[i, i] = 0
        b[i] = AB[i, -1]
    
    n = A.shape[0]
    x0 = b.copy()
    x = x0.copy()
    
    # Сохраняем корни всех итераций
    xe = [x0.tolist()]
    
    p = 0
    err = tol + 1
    
    while err >= tol:
        xp = x.copy()
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], xp[i+1:])) / A[i, i]
        err = np.max(np.abs(x - xp)) / np.max(np.abs(x0))
        p += 1
        xe.append(x.tolist())
    
    return x, p, np.array(xe)

A = np.array([[1, 0.1, -2.1, 0.2], 
              [0.2, 1, -3.2, 0.1],
              [0.13, -1.2, 1, 0.3],
              [0.1, -0.1, -0.2, 1]])

b = np.array([[-1], [-1], [2], [0.1]])

x, n, xe = solve_system_gauss_seidel(A, b , 0.0001)

print(f"Решение: {x}")
print(f"Количество итераций: {n}")
print("Корни всех итераций:")
print(xe)




def solve_system_gauss(A, b, tol=1e-5):
    """
    Решает систему линейных уравнений Ax = b методом Гаусса.
    
    Параметры:
    A (numpy.ndarray): Матрица коэффициентов системы линейных уравнений.
    b (numpy.ndarray): Вектор правых частей системы линейных уравнений.
    tol (float): Точность решения (по умолчанию 1e-5).
    
    Возвращает:
    numpy.ndarray: Решение системы линейных уравнений.
    int: Количество итераций, выполненных для достижения заданной точности.
    numpy.ndarray: Корни всех итераций.
    """
    
    # Расширенная матрица
    AB = np.hstack((A, b.reshape(-1, 1)))
    
    n = A.shape[0]
    
    # Прямой ход
    for i in range(n):
        # Поиск ведущего элемента
        max_row = i
        for j in range(i+1, n):
            if abs(AB[j, i]) > abs(AB[max_row, i]):
                max_row = j
        
        # Перестановка строк
        if max_row != i:
            AB[[i, max_row]] = AB[[max_row, i]]
        
        # Нормализация строки
        pivot = AB[i, i]
        AB[i, :] /= pivot
        
        # Исключение переменных
        for j in range(i+1, n):
            factor = AB[j, i]
            AB[j, :] -= factor * AB[i, :]
    
    # Обратный ход
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (AB[i, -1] - np.dot(AB[i, :-1], x)) / AB[i, i]
    
    return x, n, x
A = np.array([[1, 0.1, -0.1, 0.2], 
              [0.2, 1, -0.2, 0.1],
              [0.13, -0.2, 1, 0.3],
              [0.1, -0.1, -0.2, 1]])

b = np.array([[-1], [-1], [2], [0.1]])

x, n, xe = solve_system_gauss(A, b)

print(f"Решение: {x}")
print(f"Количество итераций: {n}")