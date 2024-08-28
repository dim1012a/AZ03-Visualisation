import matplotlib.pyplot as plt
import numpy as np

mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов
# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.hist(data, bins=20)
plt.xlabel('Значения случайных чисел')
plt.ylabel('Количество')
plt.title('Гистограмма нормального распределения')
plt.show()
