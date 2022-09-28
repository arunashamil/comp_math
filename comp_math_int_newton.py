import numpy as np

x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
y = np.array([0.000, 0.033, 0.067, 0.100, 0.133, 0.166, 0.199, 0.231, 0.264, 0.296, 0.327])
xo = 0.95
# Нужно найти f(0.95)

# Интерполяция полиномом Ньютона:

# Функция для нахождения разделенной разности
diffs = np.zeros([len(x),len(y)]) # таблица разделенных разностей
diffs[:,0] = y # первый столбец - просто значения функции f(x)

def div_diff(x,y):
    for i in range(1, len(x)):
        for j in range(len(x) - i):
            diffs[j][i] = (diffs[j + 1][i - 1] - diffs[j][i - 1]) / (x[j + i] - x[j])
    return diffs

t = 1
fos = div_diff(x, y)[0, :]
polynomchik = fos[0]

for i in range(1, len(x)):
    t *= (xo - x[i - 1])
    polynomchik += t * fos[i]

# Новая точка ... *барабанная дробь*

print(polynomchik)

# Получилось 0.30859112548828116