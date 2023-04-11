import numpy as np


def printer(value):
    print(value, end="\n\n")


print(np.__version__)

# convert
pyList = [12.23, 13.32, 100, 36.32]
numpyList = np.array(pyList)
print(pyList, numpyList, sep="<- pyList | numpyList ->", end="\n\n")

# matrix
matrix = np.arange(1, 10).reshape(3, 3)
print(matrix)

# zeros
zeroValues = np.zeros(10)
print(zeroValues)

zeroValues[6-1] = 11
print(zeroValues, end="\n\n")

# list
npList = np.arange(11, 38)
print(npList, end="\n\n")

# reverse
npList = npList[::-1]
print(npList, end="\n\n")

# convert
intArray = np.asfarray(np.arange(0, 4))
printer(intArray)

# try
npList = np.ones((5, 5))
npList[0:1, 0:5] = 0
print(npList)
