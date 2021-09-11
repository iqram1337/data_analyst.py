# pendahuluan numpy
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = [1, 2, 3, 4, 5]
print('')

print(f"array numpy = {a}")
a = a + 1
print("array numpy = array numpy + 1")
print(f"array numpy = {a}")
print('')

print(f"array biasa = {b}")
b = b + [1] # array biasa harus menggunakan []
print("array biasa = array biasa + 1")
print(f"array biasa = {b}")