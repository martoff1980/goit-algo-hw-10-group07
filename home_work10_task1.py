import pulp

# Ініціалізація моделі
model = pulp.LpProblem("MaxProductivity", pulp.LpMaximize)

# Визначення змінних
# Кількість продукту "Лимонад"
A = pulp.LpVariable('Limonade', lowBound=0, cat='Integer')
# Кількість продукту "Фруктовий сік"
B = pulp.LpVariable('Fruit_Juice', lowBound=0,  cat='Integer')

# Функція цілі (Максимізація виробницства)
model += A + B, "Total_Production"

# Додавання обмежень
model += 2*A + 1*B <= 100, "Water"  # Вода
model += 1*A <= 50, "Sugar"  # Сахар
model += 1*A <= 30, "Limon_Juice"  # Лімоний сік
model += 2*B <= 40, "Fruit_Pure"  # Фруктове пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Виробляти продукт {A.name} в кількості: {A.varValue}")
print(f"Виробляти продукт {B.name} в кількості: {B.varValue}")
