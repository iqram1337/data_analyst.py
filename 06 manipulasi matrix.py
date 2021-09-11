import numpy as np
print("Manipulasi Matrix".center(51, "="))

# x.shape | untuk mengetahui ukuran matrix
a = np.array([(1, 3, 5), (2, 4, 6)])
print("matrix a = ")
print(a)
print("ukuran matrix = ", a.shape)
print('')

## transpose matrix
# np.transpose(x) | x.transpose() | x.T
print("Transpose Matrix".center(30, '-'))
a = np.array([(1, 3, 5), (2, 4, 6)])
print("matrix a = ")
print(a)
print("transpose matrix a =")
print(np.transpose(a))
print("ukuran matrix a = ", a.shape)
print('')

## flatten array, vector baris (mengubah matrix menjadi vector)
# np.ravel(x) | x.ravel
print("Matrix menjadi Vector".center(30, '-'))
a = np.array([(1, 3, 6), (2, 4, 6)])
print("matrix a =")
print(a)
print("vector a = ", np.ravel(a))
print("ukuran matrix a = ", a.shape)
print('')

## reshape matrix
# x.reshape(baris, kolom) | untuk mengubah bentuk matrix
print("Reshape Matrix".center(30, '-'))
a = np.array([(1, 3, 5), (2, 4, 6)])
print("matrix a =")
print(a)
print("reshape a =")
print(a.reshape(3, 2))
print("ukuran matrix a = ", a.shape)
print('')

## resize matrix
print("Resize Matrix".center(30, '-'))
a = np.array([(1, 3, 5), (2, 4, 6)])
print("matrix a =")
print(a)
print("resize a =")
a.resize(3,2) # resize mengubah bentuk a secara permanen
print(a)
print("ukuran matrix a = ", a.shape)