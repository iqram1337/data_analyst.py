## membuat grafiik sinus
import numpy as np
import matplotlib.pyplot as plt

# theta = np.linspace(-np.pi, np.pi)
theta = np.arange(0, (4*np.pi), 0.1)
print(theta)
plt.figure('Grafik 1')

plt.plot(theta, np.sin(theta), label = 'sinus')
plt.title('Grafik Sinus')

plt.xlabel('theta')
plt.ylabel('sinus')
plt.legend()
plt.show()