""" 
This section covers 
.flatten()
ravel() 
"""

import numpy as np

x = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

""" You can use flatten to flatten your array into a 1D array. """
""" When you use flatten, changes to your new array won’t change the parent array """
""" Create array to 1D at 2D """
print(x.flatten())

""" For example """
a1 = x.flatten()
a1[0] = 99
print(x)

""" 
But when you use ravel, the changes you 
make to the new array will affect the parent array. 
"""

a2 = x.ravel()
a2[0] = 98
print(x) 

""" How to access the docstring for more information """
""" This section covers help(), ?, ?? """
print(help(max))
