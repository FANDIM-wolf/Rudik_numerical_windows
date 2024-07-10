import numpy as np

def calculate_with_simple_iterations(A, b, tol=1e-6):
    # Check for compatibility
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix should be square")
    
    n = A.shape[0]
    x = np.zeros(n)
    
    # Initialize the error
    error = np.inf
    
    while error > tol:
        x_prev = x.copy()
        
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += A[i, j] * x[j]
            
            # Check if the diagonal element is zero
            if A[i, i] == 0:
                # If the diagonal element is zero, set the corresponding element in x to 0
                x[i] = 0
            else:
                x[i] = (b[i] - sum) / A[i, i]
        
        # Calculate the error
        error = np.linalg.norm(x - x_prev)
    
    return x

# Example of use
a = np.array([[0, 2.1, -0.21], 
              [0.1, 1.12, -0.24],
              [0.2, 1.6, 0.4]])

b = np.array([[-1], [-0.21], [0.21]])


x = calculate_with_simple_iterations(a, b, tol=1e-4)
print(x)
import numpy as np

def solve_system(a, b, x0, tol=0.01):
    """
    Решает систему линейных уравнений Ax = b методом простых итераций.
    
    Параметры:
    a (numpy.ndarray): Матрица коэффициентов системы линейных уравнений.
    b (numpy.ndarray): Вектор правых частей системы линейных уравнений.
    x0 (numpy.ndarray): Начальное приближение для решения.
    tol (float): Точность решения (по умолчанию 0.01).
    
    Возвращает:
    numpy.ndarray: Решение системы линейных уравнений.
    int: Количество итераций, выполненных для достижения заданной точности.
    """
    
    # Вычисляем максимальный элемент матрицы a
    t = np.max(np.abs(a))
    
    # Если максимальный элемент больше 0.5, уменьшаем точность
    if t > 0.5:
        tol *= (1 - t) / t
    
    x0 = np.array(x0)
    x1 = a @ x0 + b
    n = 0
    
    # Сохраняем корни всех итераций
    xe = [x0.tolist()]
    
    while np.linalg.norm(x1 - x0) > tol:
        x0 = x1
        x1 = a @ x0 + b
        n += 1
        xe.append(x1.tolist())
    
    return np.array(x1), n, np.array(xe)
a = np.array([[1, 2.1, -0.21], 
              [0.1, 1.12, -0.24],
              [0.2, 1.6, 0.4]])

b = np.array([[-1], [-0.21], [0.21]])

x0 = b

x, n, xe = solve_system(a, b, x0)

print(f"Решение: {x}")
print(f"Количество итераций: {n}")
print("Корни всех итераций:")
print(xe)


def simple_iter(A, B):
    x = np.zeros(len(A)) #vector column 
    D = np.diag(A)  #diagonal matrix
    R = A - np.diagflat(D) # diff between A and diag matrix
    e = 0.0001
    iters = 0

    a = np.sum(R,axis=1) #adds val-s by row 
    a = a/D  #divides by diag matrix
    while e<1:
        e = np.linalg.norm(a) #finds vector norm 
        if e<1:
            x2 = (B - np.dot(R,x))/D
            x = x2
        a = x*a
        iters+=1
    print(iters," ",x)
    return x,iters
x , iter = simple_iter(a,b)
print(x)