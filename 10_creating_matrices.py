import numpy as np

data = np.array([[1, 2], [3, 4], [5, 6]])
print(data)

""" Indexing """
print(data[0, 1])
print(data[1:3])

""" Slicing """
print(data[0:2, 0])

""" You can aggregate matrices the same way you aggregated vectors """
print(data.sum())
print(data.min())
print(data.max())

data1 = np.array([[1, 2], [5, 3], [4, 6]])
print(data1.max(axis=0))

""" Maximum value of all arrays  """
print(data1.max(axis=1))

data = np.array([[1, 2], [3, 4]])
ones = np.array([[1, 1], [1, 1]])
print(data + ones)

""" You can do these arithmetic operations on matrices of different sizes """
data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
print(data + ones_row)

""" Create Generation """
rng = np.random.default_rng(12345) 
print(rng.integers(low=3, high=10, size=50))

""" Create matrix """
print(np.ones((3, 2)))
print(np.zeros((3, 2)))
print(rng.random((3, 2)))