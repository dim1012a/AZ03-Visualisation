import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(50)
y = np.random.randn(50)

plt.scatter(x, y)
plt.xlabel('Случайный набор X')
plt.ylabel('Случайный набор Y')
plt.title('Диаграмма рассеяния двух наборов случайных данных')
plt.show()
