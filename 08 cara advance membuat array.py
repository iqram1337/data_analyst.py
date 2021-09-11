import numpy as np

## membuat matrix dengan tipe data tertentu
print("matrix tipe data float".center(30,'-'))
a = np.array(([1, 3, 5], [2, 4, 6]), dtype = float)
print(a)
print('')

## membuat array dengan menggunakan function
print("array dengan fungsi".center(31, '-'))
def kuadrat(baris, kolom):
    return kolom**2

b = np.fromfunction(kuadrat, (1,10), dtype = int)
print(b)
print('')

## membuat array dengan menggunakan function
print("array dengan fungsi".center(31, '-'))
def penjumlahan(baris, kolom):
    return (baris+kolom)

c = np.fromfunction(penjumlahan, (3, 4), dtype = int)
print(c)
print('')

## membuat array atau matrix dengan menggunakan iterable
print("array dengan iterasi".center(31, '-'))

itera = (i*i for i in range(5))

d = np.fromiter(itera, dtype = int)
print(d)
print('')


## multitype array
print("multitype array".center(31, '-'))

dtipe = [('nama', 'S10'), ('nomor', int)]
data = [('iqram', 2), ('haris', 7), ('fahromi', 1)]
e = np.array(data, dtype = dtipe)
print(e)
print(data[0])