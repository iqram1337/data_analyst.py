# membuat grafik lingkaran
import numpy as np
import matplotlib.pyplot as plt

# jari-jari lingkaran:
r = 1

# jumlah sisi/tepi:
n = 64

# membuat sudut theta:
th = np.linspace(0, (2*np.pi), n+1)

# persamaan titik x dan y lingkaran:
x = r*np.cos(th)
y = r*np.sin(th)

# menampilkan lingkaran
plt.axis('equal')
plt.grid()
plt.plot(x, y)
plt.show()