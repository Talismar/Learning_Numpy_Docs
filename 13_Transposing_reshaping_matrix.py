""" This section covers arr.reshape(), arr.transpose(), arr.T """

""" 
It’s common to need to transpose your matrices.
NumPy arrays have the property T that allows you to transpose a matrix.
"""
import numpy as np

data = np.array([1,2,3,4,5,6])

print(data.reshape(2, 3))
print(data.reshape(3, 2))

""" 
You can also use .transpose() to reverse or 
change the axes of an array according to the values you specify. 
"""
data = np.array([1,2,3,4,5,6]).reshape((2, 3))
print(data.transpose())
""" Or used """
print(data.T)