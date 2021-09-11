import numpy as np
import matplotlib.pyplot as plt

## rumus: x(t) =  A cos (2pi [f] t)
A = 1.27
f = 2.55

t = np.arange(0, 10, 0.01)

x = A*np.cos(2*np.pi*f*t)
plt.axis([0, 2, -2, 2])
plt.grid()
plt.plot(t, x)
plt.show()