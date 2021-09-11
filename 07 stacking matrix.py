from typing import ByteString
import numpy as np

## menumpuk array dengan array, menjadi matrix
print("Menumpuk Matrix".center(31, '='))
a = np.array([1, 3, 5])
b = np.array([2, 4, 6])
print(f"arr a = {a}")
print(f"arr b = {b}")
print('')

# menumpuk matrix secara horizontal
print("Horizontal".center(20, '-'))
print("arr a + arr b =")
c = np.hstack((a, b))
print(c)
print('')

# menumpuk matrix secara vertikal
print("Vertikal".center(20, '-'))
print("arr a + arr b =")
c = np.vstack((a, b))
print(c)
print('\n\n')

## menumpuk matrix dengan matrix, menjadi matrix
print("Matrix Satu dan Nol".center(31, '='))
x = np.zeros((2,2))
y = np.ones((2,2))
print("matrix x =")
print(x)
print("matrix y =")
print(y)
print('')

# scr horizontal
print("Horizontal".center(20, '-'))
print("matrix x + matrix y =")
z = np.hstack((x, y))
print(z)
print('')

# scr vertikal
print("Vertikal".center(20, '-'))
print("matrix x + matrix y =")
z = np.vstack((x, y))
print(z)