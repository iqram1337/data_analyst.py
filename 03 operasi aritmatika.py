import numpy as np

## array list python
print("List Python".center(41,"="))
a = [1, 2, 3]
b = [6, 7, 8]
print(f"arr a + arr b = {a} + {b}")
c = a + b
print("              =", c)
print('')


## array numpy
## ELEMENTWISE operation

# penjumlahan
print("Array Numpy".center(41,"="))
anp = np.array([1, 2, 3])
bnp = np.array([6, 7, 8])
print(f"arr a + arr b = {anp} + {bnp}")
cnp = anp + bnp
print("              =", cnp)
print('')

# pengurangan
anp = np.array([1, 2, 3])
bnp = np.array([6, 7, 8])
print(f"arr a - arr b = {anp} - {bnp}")
cnp = anp - bnp
print("              =", cnp)
print('')

# pembagian
anp = np.array([1, 2, 3])
bnp = np.array([6, 7, 8])
print(f"arr a / arr b = ({anp} / {bnp})")
cnp = anp / bnp
print("              =", cnp)
print('\n')

# perkalian
anp = np.array([1, 2, 3])
bnp = np.array([6, 7, 8])
print(f"arr a x arr b = ({anp} x {bnp})")
cnp = anp * bnp
print("              =", cnp)
print('')

# kuadrat
bnp = np.array([6, 7, 8])
print(f"arr b         = ({bnp})^2")
cnp = bnp**2
print("              = ", cnp)
print('\n')


## multidimensi array numpy
print("Multidimensi Array NumPy".center(41,"="))
mda = np.array([(1, 2, 3), (4, 5, 6)])
mdb = np.array([(2, 2, 2), (6, 7, 8)])
print(f"arr a =")
print(mda)
print('')
print(f"arr b =")
print(mdb)
print("-----------------(x)")
mdc = mda * mdb
print(mdc) #!!! bukan perkalian matrix, hanya perkalian elementwise biasa