import scipy.integrate as spi
import pulp
import numpy as np


def func_quad():
    # Визначте функцію, яку потрібно інтегрувати,
    # наприклад, f(x) = x^2
    def f(x):
        return x**2

    # Визначте межі інтегрування, наприклад, від 0 до 2
    a = 0  # нижня межа
    b = 2  # верхня межа

    # Обчислення інтеграла
    result, error = spi.quad(f, a, b)

    return {"result": result, "error": error}


def func_monte_carlo():
    def f(x):
        return x ** 2

    a = 0  # Нижня межа
    b = 2  # Верхня межа
    N = 400  # кількість вимирів
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, N)
    # print(x)
    y = f(x)
    koeff = (b-a)/N

    # Ініціалізація моделі
    # model = pulp.LpProblem("QuadFunction", pulp.LpMaximize)
    X = pulp.LpVariable.dict('X', x, pulp.LpContinuous)
    Y = pulp.LpVariable.dict('Y', y, lowBound=pulp.LpContinuous)

    Sum = pulp.lpSum(k for k in Y.keys() if k >= f(a) and k <= f(b))
    # Площа: S=((b-a)/N)*Sum
    S = koeff*Sum

    return S


quad = func_quad()
print("Інтеграл: ", quad["result"])

monte_carlo = func_monte_carlo()
print("Інтеграл методом Монте-Карло: ", monte_carlo)
