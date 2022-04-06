""" 
This section covers slicing and indexing
np.vstack()
np.hstack()
np.hsplit()
.view()
copy()
"""

""" You can easily create a new array from a section of an existing array. """

import numpy as np

""" 
You can also stack two existing arrays, both vertically and horizontally. 
Let’s say you have two arrays, a1 and a2 
"""

a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])

""" You can stack them vertically with vstack: """
print(np.vstack((a1, a2)))

""" Or horizontally """
print(np.hstack((a1, a2)))

""" You can split an array into several smaller arrays using hsplit """
x = np.arange(1, 11).reshape(2, 5)

print(np.hsplit(x, 1))


""" 
Now we create an array b1 by slicing a and modify the first element of b1. 
This will modify the corresponding element in a as well! 
"""
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

b1 = a[0, :]
b1[0] = 99
print(b1)
print(a)

""" Using the copy method will make a complete copy of the array and its data (a deep copy).  """
b2 = a.copy()
print(b2)