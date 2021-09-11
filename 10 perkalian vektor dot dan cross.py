import numpy as np

# perkalian vektor dot product
print("Perkalian Dot Product".center(41, "="))
va = np.array([1, 3, 5])
vb = np.array([2, 4, 6])

print(f"vek a = {va}")
print(f"vek b = {vb}")
vc = np.dot(va, vb)
print(f"vek a 'dot' vek b = {vc}")
print('')


# perkalian vektor cross product
print("Perkalian Cross Product".center(41, "="))
va2 = np.array([1, 3, 5])
vb2 = np.array([2, 4, 6])

print(f"vek a = {va2}")
print(f"vek b = {vb2}")
vc2 = np.cross(va2, vb2)
print(f"vek a 'cross' vel b = {vc2}")
print('')