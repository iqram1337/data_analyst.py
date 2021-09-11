import numpy as np

print("Sorting Matrix".center(31, '='))
a = np.floor(np.random.rand(3,3)*10)
print("matrix a:")
print(a)
print("ukuran matrix = ", a.shape)

# mencari nilai max dari matrix a
print("max a = ", np.max(a))
# mencari nilai min dari matrix a
print("min a = ", np.min(a))

# mencari posisi index nilai max dari matrix a
print("posisi max a berada di indeks ke = ", np.argmax(a))
# mencari posisi index nilai min dari matrix a
print("posisi min a berada di indeks ke = ", np.argmin(a))
print('\n')

# sorting
print("matrix a:")
print(a)
print("mengurutkan matrix a:")
print(np.sort(a))
print("mengurutkan indeks matrix a:")
print(np.argsort(a))