import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import numpy as np


def f(x):
    return -12*(x**4)*np.sin(np.cos(x))-18*x**3+5*x**2+10*x-30


x = np.arange(-2.5, 2.5, 0.01)
x1 = fsolve(f, -2)
x2 = fsolve(f, 2)
roots = [*x1, *x2]
roots = [round(x, 3) for x in roots]
min_y = min(f(x))


def y(x, res_y):
    return -12*(x**4)*np.sin(np.cos(x))-18*x**3+5*x**2+10*x-30-res_y

min_x = fsolve(y,1, min_y)


plt.plot(x, f(x), 'r-')
plt.axhline(0,color='grey')
plt.axvline(0,color='grey')
plt.plot(x1, f(x1), 'ro', label=f'Корни уравнения: {roots}')
plt.plot(x2, f(x2), 'ro')
plt.plot(min_x, f(min_x), 'gx', label=f'Вершина: ({round(min_x[0], 3)}, {round(min_y, 3)} )')

# Функция f>0 и f<0:

x = np.arange(-2.5, x1, 0.01)
plt.plot(x, f(x), 'y-', label='Функция > 0')
x = np.arange(x1, x2, 0.01)
plt.plot(x, f(x), 'g-', label='Функция < 0')
x = np.arange(x2, 2.5, 0.01)
plt.plot(x, f(x), 'y-')
plt.legend()
plt.grid()


x = np.arange(-1, 0.5, 0.01)
min_y1 = min(f(x))
min_x1 = fsolve(y, -1, min_y1)

x = np.arange(0, 1, 0.01)
min_y2 = max(f(x))
min_x2 = fsolve(y, 0, min_y2)

x = np.arange(x1, min_x1, 0.01)
plt.plot(x, f(x), 'y-', label='Функция убывает')

x = np.arange(min_x1, min_x2, 0.01)
plt.plot(x, f(x), 'g-', label='Функция возрастает')

x = np.arange(min_x2, min_x, 0.01)
plt.plot(x, f(x), 'y-')

x = np.arange(min_x, x2, 0.01)
plt.plot(x, f(x), 'g-')

plt.axhline(0,color='grey')
plt.axvline(0,color='grey')
plt.legend()
plt.grid()
