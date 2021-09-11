import numpy as np
print("Persamaan Linear".center(40, '='))

# dik: y1 = 23, y2  = 14, a =([2 3], [1 2])
# dit: x1 dan x2
# y = a.x
# x = a^(-1).y

## urutan penyelesaian
a = np.array([(2, 3), (1, 2)])
y = np.array([23, 14])

print("X: ???")
print("A:")
print(a)
print("Y:")
print(y)
print('\n(1) Y = A X')
print('(2) X = A^(-1) Y')
print('')

a_inv = np.linalg.inv(a)
print("A^(-1):")
print(a_inv)
print('')

## penyelesaian
x1 = np.dot(a_inv, y)
print(f"X = {x1}")
print('')
# cara lain
x2 = np.linalg.solve(a, y)
print(f"X = {x2}")
