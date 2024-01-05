# Для следующих данных определите коэффициенты b0 и bx в зависимости
import numpy as np

x = np.array([-2, -1, 1, 2, 3]).reshape(-1, 1)
y = np.array([-1.34, 0.94, 5.5, 7.78, 10.06])


from sklearn.linear_model import LinearRegression

# Создаем и обучаем модель
model = LinearRegression()
model.fit(x, y)

# Получаем коэффициенты b0 и bx
b0 = model.intercept_
bx = model.coef_[0]

print(b0, bx)
