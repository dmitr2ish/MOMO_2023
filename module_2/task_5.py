import matplotlib.pyplot as plt  # библиотека MatPlotLib для визуализации
import pandas as pd  # Библиотека Pandas для работы с табличными данными
import sklearn.datasets as ds  # модуль библиотеки scikit-learn про игрушечные данные
from sklearn.datasets import fetch_openml  # функция библиотеки scikit-learn для загрузки данных с сайта OpenML

from sklearn import preprocessing as prep  # модуль предварительной обработки данных от scikit-learn

# Применение обратной формулы стандартизации:
def original_value(z, mean, std):
    return z * std + mean

# Ознакомьтесь с блокнотом про предварительную обработку данных в scikit-learn:
# https://colab.research.google.com/drive/1q3HsjCPgl9gXwiNxI8OTkpPId8a5QcPD?usp=sharing.

# В этом блокноте мы выполняем различную предварительную обработку набора данных по кредитованию.
# Среди числовых признаков там происходит стандартизация числовых признаков 'duration', 'credit_amount' и 'age'.

# Проанализируйте результаты стандартизации и ответьте на вопрос: какому значению в оригинальном распределении признаков
# соответствуют следующие значения после стандартизации.
# В ответе укажите целую часть.

plt.style.use('dark_background')  # для модных черных рисунков

# воспользуемся функцией fetch_openml для загрузки данных с сайта OpenML
# для этого нам необходимо знать имя набора данных и версию
data = fetch_openml('credit-g', version=1, return_X_y=False)  # загружаем данные в виде словаря
# альтернативно можно было прописать  что хотим чтобы скачалось в формате признаки/целевые метки (return_X_y = True)

print(data.keys())  # смотрим на ключи в словаре

DF_OML = pd.DataFrame(data.data, columns=data.feature_names)  # взяли из словаря по ключевым словам data и feature_names
DF_OML['Target'] = data.target  # добавляем колонку Target на основе целевых меток

# Вычисление среднего значения
age_mean = DF_OML['age'].mean()
print(age_mean)
# стандартного отклонения
age_std = DF_OML['age'].std()
print(age_std)
# Значение признака после стандартизации
age_z = 2
# Применение обратной формулы
print(original_value(age_z, age_mean, age_std))
print()

duration_mean = DF_OML['duration'].mean()
print(duration_mean)
duration_std = DF_OML['duration'].std()
print(duration_std)
duration_z = -1
print(original_value(duration_z, duration_mean, duration_std))
print()

credit_amount_mean = DF_OML['credit_amount'].mean()
print(credit_amount_mean)
credit_amount_std = DF_OML['credit_amount'].std()
print(credit_amount_std)
credit_amount_z = 1
print(original_value(credit_amount_z, credit_amount_mean, credit_amount_std))


