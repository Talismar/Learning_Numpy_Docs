""" Using arr.reshape() will give a new shape to an array without changing the data. """

import numpy as np

a = np.arange(6)
print(a)

""" You can use reshape() to reshape your array.  """
b = a.reshape(3, 2)
print(b)

""" With np.reshape, you can specify a few optional parameters: """
"""  C means to read/write the elements using C-like index order """
print(np.reshape(a, newshape=(1, 6), order='C'))

"""  returns the array, flattened """
print(b.ravel())

