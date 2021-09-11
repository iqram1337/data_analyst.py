## membuat grafik cosinus
import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(1, np.pi*4, 0.1)
print(theta)

plt.plot(theta, np.cos(theta), label = 'cosinus')
plt.title('Grafik Cosinus')

plt.ylabel('cosinus')
plt.xlabel('theta')
plt.legend()
plt.show()