import numpy as np
print("Array Numpy".center(41, "="))
a = np.arange(10)**2
print(f"array a = {a}")
print('')

# mengambil nilai
print("elemen ke-1 dari a = ", a[0])
print("elemen ke-5 dari a = ", a[4])
print("elemen terakhir a  = ", a[-1])
print('')

# slicing
print("elemen dari 1-6     = ", a[0:6])
print("elemen dari 4-akhir = ", a[3:])
print("elemen dari awal-4  = ", a[:3])
print('')

# iterasi
for i in a:
    print("nilai = ", i) 