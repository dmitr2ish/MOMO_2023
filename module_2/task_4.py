import pandas as pd

DF = pd.read_csv('https://raw.githubusercontent.com/dayekb/Basic_ML_Alg/main/cars_moldova_no_dup.csv', delimiter=',')

# Подготовьте ответы на следующие вопросы.
#
# Для решения этого задания вам необходимо воспользоваться методами groupby для агрегации данных, sort_values для сортировки таблицы.
cat_columns = []  # создаем пустой список для имен колонок категориальных данных
num_columns = []  # создаем пустой список для имен колонок числовых данных

for column_name in DF.columns:  # смотрим на все колонки в DataFrame
    if (DF[column_name].dtypes == object):  # проверяем тип данных для каждой колонки
        cat_columns += [column_name]  # если тип объект - то складываем в категориальные данные
    else:
        num_columns += [column_name]  # иначе - числовые

# важно: если признак категориальный, но хранится в формате числовых данных, тогда код не сработает корректно

# выводим результат
print('Категориальные данные:\t ', cat_columns, '\n Число столблцов = ', len(cat_columns))

print('Числовые данные:\t ', num_columns, '\n Число столблцов = ', len(num_columns))

# 1. Найдите марку автомобилей (столбец Make) с наибольшей средней стоимостью (столбец Price(euro))
grouped = DF.groupby('Make') # группировка данных
avg_price = grouped['Price(euro)'].mean() # расчет среднего для столбца Price
sorted_price = avg_price.sort_values(ascending=False) # сортировка
print(sorted_price.index[0])

# 2. Найдите модель автомобилей (столбец Model) с наибольшим средним пробегом (столбец Distance).
avg_distance = DF.groupby('Model')['Distance'].mean()
sorted_dist = avg_distance.sort_values(ascending=False)
print(sorted_dist.index[0])
# 3. Найдите тип топлива (столбец Fuel_type) с наибольшим средним годом выпуска (столбец Year).
avg_year = DF.groupby('Fuel_type')['Year'].mean()
max_avg_year = avg_year.sort_values(ascending=False).index[0]
print(max_avg_year)