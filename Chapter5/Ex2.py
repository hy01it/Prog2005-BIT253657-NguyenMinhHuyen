import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
plt.plot(x, x**2, label="y = x^2", color="blue")
plt.plot(x, x**3, label="y = x^3", color="red")
plt.title("Đồ thị hàm số")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
