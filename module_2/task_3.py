import pandas as pd

DF = pd.read_csv('https://raw.githubusercontent.com/dayekb/Basic_ML_Alg/main/cars_moldova_no_dup.csv', delimiter=',')

# Набор данных Car Moldova после удаления дубликатов: https://raw.githubusercontent.com/dayekb/Basic_ML_Alg/main/cars_moldova_no_dup.csv.

# Подготовьте ответы на следующие вопросы.

# 1. Укажите количество автомобилей, для которых тип кузова — Universal (столбец Style) и стоимость выше 10000 евро (столбец Price(euro)).
df_universal_more_than_10000 = DF[(DF['Style'] == 'Universal') & (DF['Price(euro)'] > 10000)]
print(df_universal_more_than_10000.describe())

# 2. Укажите количество автомобилей, для которых марка автомобиля — Mercedes (столбец Make) и год выпуска — раньше 1980 года (столбец Year).
df_mersedes_less_than_1980 = DF[(DF['Make'] == 'Mercedes') & (DF['Year'] < 1980)]
print(df_mersedes_less_than_1980.describe())