import numpy as np
import matplotlib.pyplot as plt

a = np.array([[25, 5, 1], [64, 8, 1], [144, 12, 1]])
b = np.array([106.8, 177.2, 279.2])

print("A*X = B")
print('')

print("matrix a:")
print(a)
print('\n')

print("matrix b:")
print(b)
print('\n')

print('a invers:')
print(np.linalg.inv(a))
print('\n')

print(f"a, b, c:", np.linalg.inv(a).dot(b))
