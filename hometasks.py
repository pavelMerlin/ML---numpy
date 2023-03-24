import numpy as np


print(np.__version__)

l = [12.23, 13.32, 100, 36.32]
print("Original List:", l)
a = np.array(l)
print("One-dimensional NumPy array: ", a)

x = np.arange(2, 11).reshape(3, 3)
print(x)