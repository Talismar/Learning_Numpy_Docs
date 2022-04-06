""" 
This section covers
addition
subtraction
multiplication
division
"""
import numpy as np

""" You can add the arrays together with the plus sign. """
data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(data + ones)

print(data - ones)
print(data * ones)
print(data / ones)
print(data ** ones)

print(data.sum())

b = np.array([[1, 1], [2, 2]])
print(b.sum(axis=0))
print(b.sum(axis=1))

"""  get the average """
print(np.array([1,2,3,4,5]).mean())
print(np.array([1,2,3,4,5]).min())
print(np.array([1,2,3,4,5]).max())

""" std to get the standard deviation """
print(np.array([1,2,3,4,5]).std())

""" prod to get the result of multiplying the elements together """
print(np.array([1,2,3,4,5]).prod())