""" 
This section covers
np.newaxis
np.expand_dims 
"""

""" 
You can use np.newaxis and np.expand_dims
to increase the dimensions of your existing array. 
"""

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)

""" Add a new axis """
a2 = a[np.newaxis, :]
print(a2.shape)
# print(a2)

col_vector = a[:, np.newaxis]
# print(col_vector.shape)
# print(col_vector)

""" 
You can also expand an array 
by inserting a new axis at a specified position with np.expand_dims. 
"""
a = np.array([1, 2, 3, 4, 5, 6])

b = np.expand_dims(a, axis=1)
print(b)

