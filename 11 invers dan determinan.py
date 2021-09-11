import numpy as np

# membuat inverse matrix dan determinan
print("Inverse Matrix".center(30, "="))
a = np.array([(1, -1), (1, 1)])
print("A:")
print(a)
a_det = np.linalg.det(a) # determinan
print(f"det A = {a_det}")
print('')
a_inv = np.linalg.inv(a) # inverse
print("A^(-1):")
print(a_inv)
print('')

# pembuktian
print("Pembuktian".center(30, '='))
print("A x A^(-1):")
print(np.dot(a, a_inv))