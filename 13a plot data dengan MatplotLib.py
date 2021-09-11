# visualisasi data dengan matplotlib
import numpy as np
import matplotlib.pyplot as plt

## persamaan garis linear
# y = 2x + 3
print("Membuat Grafik Linear".center(40, '='))
x = np.arange(1,11)
y = (2*x) + 3 
print("y = 2x +3")
print('')
print(f"x = {x}")
print(f"y = {y}")
print('\n')

plt.figure("y = 2x + 3")
plt.plot(x, y) # menampilkan grafik
#plt.show()


## persamaan lingkaran
# x = r cos(theta) & y = r sin(theta)
print("Membuat Grafik Linear".center(40, '='))
r = 5
th = np.linspace(0, (2*np.pi), 100)
x2 = (r*np.cos(th))
y2 = (r*np.sin(th))
print(f"x = {x2}")
print(f"y = {y2}")

plt.figure("Lingkaran")
plt.plot(x2, y2) # menampilkan grafik
plt.show()
