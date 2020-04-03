from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

def func(x, a, b):
    return a * np.exp(b * x)

x_data = np.linspace(1, 15, 15)
y_data = np.array([1, 1, 5, 5, 6, 18, 47, 98, 192, 359, 670, 1236, 1529, 1872, 2433])

params, params_covariance = optimize.curve_fit(func, x_data, y_data)


plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, func(x_data, params[0], params[1]),
         label='Fitted function')

plt.legend(loc='best')

plt.show()