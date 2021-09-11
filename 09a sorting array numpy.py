import numpy as np

print("Sorting Array".center(31, '='))
a = np.floor(np.random.rand(5)*10)
print(f"arr a = {a}")

# mencari nilai max dari arr a
print("max a = ", np.max(a))
# mencari nilai min dari arr a
print("min a = ", np.min(a))

# mencari posisi index nilai max a dari arr a
print("posisi max a berada di index ke = ", np.argmax(a))
# mencari posisi index nilai min a dari arr a
print("posisi min a berada di index ke = ", np.argmin(a))
print('')

# sorting arr
print(f"arr a = {a}")
print("mengurutkan arr a = ", np.sort(a))
print("mengurutkan index a = ", np.argsort(a))