import numpy as np

""" 
This section covers
ndarray.ndim - will tell you the number of axes, or dimensions, of the array.
ndarray.size - will tell you the total number of elements of the array. 
ndarray.shape -  will display a tuple of integers that indicate the number of elements stored along each dimension of the array. 
"""

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

""" To find the number of dimensions of the array, run """
# print(array_example.ndim)

""" To find the total number of elements in the array, run """
# print(array_example.size)

""" find the shape of your array, run """
print(array_example.shape)