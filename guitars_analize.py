import pandas as pd
import matplotlib.pyplot as plt

guit = pd.read_csv('guitars.csv')
print(guit.head())
print()
print(guit.info())
print()

guit_clear = guit.dropna() # убираем строки с пустыми значениями
print(guit_clear.info())
print()

print("Средняя цена на гитары равна  ", guit_clear['Price'].mean())

#Выводим гистограмму
plt.hist(guit_clear['Price'], bins=20)
plt.title('Гистограмма цен на гитары')
plt.xlabel('Цены на гитары')
plt.ylabel('Количество')
plt.show()
