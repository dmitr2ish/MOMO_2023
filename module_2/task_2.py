import pandas as pd

# Набор данных Car Moldova после удаления дубликатов: https://raw.githubusercontent.com/dayekb/Basic_ML_Alg/main/cars_moldova_no_dup.csv.

# Подготовьте ответы на следующие вопросы.
# 1. Сколько строк в наборе данных?
DF = pd.read_csv('https://raw.githubusercontent.com/dayekb/Basic_ML_Alg/main/cars_moldova_no_dup.csv', delimiter=',')
print(DF.describe())
print()
# 2. Укажите медианное значение столбца с объемом двигателя (Engine_capacity(cm3)). В ответе укажите целую часть.
print(DF['Engine_capacity(cm3)'].median())
print()
# 3. Укажите наиболее часто встречающийся тип топлива (Fuel_type) и число таких автомобилей. В первом ответе укажите строку без кавычек.
print(DF.Fuel_type.value_counts())
