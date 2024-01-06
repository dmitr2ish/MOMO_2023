import numpy as np
# Вы получили веса модели b = {3,-2,2}. В модели не используется смещение (b0).
# Оцените предсказание модели для следующих значений параметров X.

# x1 x2 x3
# 0 0 0.5
# 0 -2 2
# 1 1 1
# 1 -1 1


# Веса модели
weights = np.array([3, -2, 2])

# Значения параметров X
X = np.array([
    [0, 0, 0.5],
    [0, -2, 2],
    [1, 1, 1],
    [1, -1, 1]
])

# Расчет предсказаний модели
predictions = X.dot(weights)

print(predictions)

#Эти значения получены путем умножения значений параметров на соответствующие веса модели и суммирования результатов,
# так как смещение b0 в модели не используется.