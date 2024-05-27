import numpy as np
import matplotlib.pyplot as plt

# Вхідні дані для варіанту 8
X = np.array([6, 7, 8, 9, 10, 12])
Y = np.array([2, 3, 3, 4, 6, 5])

# Функція для обчислення коефіцієнтів лінійної регресії
def linear_regression(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return m, c

# Обчислення коефіцієнтів
slope, intercept = linear_regression(X, Y)

# Функція для побудови графіка
def plot_regression_line(x, y, slope, intercept):
    plt.scatter(x, y, color='red', marker='o', label='Експериментальні дані')
    regression_line = slope * x + intercept
    plt.plot(x, regression_line, color='blue', label='Лінія регресії')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

# Побудова графіка
plot_regression_line(X, Y, slope, intercept)
