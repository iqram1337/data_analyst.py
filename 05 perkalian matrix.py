import numpy as np
print("Perkalian Matrix".center(41, "="))

# cara pertama
a = np.array([(1, 2, 3), (6, 7, 8)])
b = np.array([(2, 4, 1), (1, 3, 5), (1, 2, 1)])
print("matrix a =")
print(a)
print("matrix b =")
print(b)
print("----------------(x)")
c = np.dot(a, b) # np.dot(matrix1 x matrix2)
print(c)
print("\n")


# cara kedua
a = np.array([(1, 3), (5, 7)])
b = np.array([(2, 4), (6, 8)])
print("matrix a =")
print(a)
print("matrix b =")
print(b)
print("----------------(x)")
c = a.dot(b) # matrix1.dot(matrix2)
print(c)