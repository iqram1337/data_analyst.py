## test soal pk yudist
import numpy as np
import matplotlib.pyplot as plt

## rumus: x(t) = x0 cos(omega t)
# omega = sqrt(k/m)

k, m = 100, 1
t = np.arange(0, 1, 0.01)
x0 = 0.1
omega = np.sqrt(100/1)

plt.title('Gerak Harmonik Sederhana')

plt.plot(t, (x0*np.cos(omega*t)), label = 'perpindahan')

plt.axis([0, 1, -0.15, 0.15])
plt.grid()
plt.legend()

plt.xlabel('t(detik)')
plt.ylabel('x(cm)')

plt.show()