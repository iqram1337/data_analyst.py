import numpy as np

# membuat vector
a = np.array([1, 2, 3, 4, 5])
print(f"vector array     = {a}")
a = a + 1
print(f"a = a + 1 vektor = {a}")
print('')

# membuat vector dengan range
b = np.arange(1, 10)
c = np.arange(1, 10, 2)
print(f"array range (1, 10)    = {b}")
print(f"array range (1, 10, 2) = {c}")
print('')

# membuat linspace 
d = np.linspace(0, 100, 5) # (start = , stop = , num = )
e = np.linspace(1, 10, 4)
print(f"array linspace = {d} (0, 100, 5)") 
print(f"array linspace = {e} (1, 10 ,4)")
print('')

# array multidimensional / matrix
f = np.array([ ( 1, 2, 3), (6, 7, 8)])
print(f)
subdata = f[1] [2]
print(f"index ke-[1] [2] = {subdata}")
print('')
print(f)
f = f + 1
print(f"array = array + 1")
print(f)
print('')

# matrix dengan nilai nol
g = np.zeros((3, 3))
print(f"""matrix nol = 
{g}""")
print('')

# matrix dengan nilai satu
h = np.ones((3, 3))
print(f"""matrix satu = 
{h}""")
print('')

# matrix identitas
i = np.identity(3)
print(f"""matrix identitas = 
{i}""")
print('')
j = np.eye(3)
print(f"""matrix identitas = 
{j}""")