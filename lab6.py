# Ініціалізація параметрів
theta1 = 5
theta0 = 7

# Навчальна пара
x1 = 1
y1 = 1

# Швидкість навчання
alpha = 0.1

# Точність
epsilon = 0.25


# Функція для передбачення значення y
def predict(x, theta1, theta0):
    return x * theta1 + theta0


# Функція для обчислення похибки
def compute_error(y_pred, y_true):
    return y_pred - y_true


# Функція для оновлення параметрів theta1 і theta0
def update_parameters(theta1, theta0, x, y_true, alpha):
    y_pred = predict(x, theta1, theta0)
    error = compute_error(y_pred, y_true)
    theta1 -= alpha * error * x
    theta0 -= alpha * error
    return theta1, theta0, error


# Головний цикл градієнтного спуску
iterations = 0
while True:
    iterations += 1
    theta1, theta0, error = update_parameters(theta1, theta0, x1, y1, alpha)
    print(f'Iteration {iterations}: theta1 = {theta1}, theta0 = {theta0}, error = {error}')

    # Умови завершення
    if abs(error) <= epsilon:
        break

print(f'Знайдені параметри: theta1 = {theta1}, theta0 = {theta0}')
