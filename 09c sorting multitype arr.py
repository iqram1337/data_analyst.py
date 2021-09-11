import numpy as np

print("Sorting Multitype Array".center(42, "="))
dtipe = [('nama', 'S10'), ('tinggi', int)]
data = [('iqram', 100), ('haris', 180), ('fahromi', 165)]

a = np.array(data, dtype = dtipe)
print("arr a:")
print(a)
print('')
# mengurutkan berdasarkan tinggi badan
print("mengurutkan berdasarkan tinggi:")
print(np.sort(a, order = 'tinggi'))

# mengurutkan berdarakan nama
print("mengurutkan berdasarkan nama:")
print(np.sort(a, order = "nama"))
print('')