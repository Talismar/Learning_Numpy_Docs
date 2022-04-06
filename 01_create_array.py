"To create"

""" 
This section covers 
np.array()
np.zeros() 
np.ones() 
np.empty()
np.arange()
np.linspace()
"""

""" All you need to do to create a simple array is pass a list to it. """
""" Se voce quiser criar um array simples, passe uma lista para ele """

import numpy as np

lista = [5,6,4,8,9,6]
print(np.array(lista))
# print(np.array([5,4,3,2,1]))
# print(np.zeros(5))
# print(np.ones(5))
# print(np.empty(5))
# print(np.arange(5))
# print(np.arange(5,20,2))

"create an array with values that are spaced linearly in a specified interval"
# print(np.linspace(0,10,num=5))
# print(np.linspace(0,10,num=5, dtype=np.int64))

a = np.arange(12)**2
i = np.array([1, 1, 3, 8, 5]) 
print(a[i])

j = np.array([[3, 4], [9, 7]]) 
print(a[j])

a = np.arange(5)
a[[1, 3, 4]] = 0
a[[1, 3, 4]] = [1,90,120]
print(a)

c = np.arange(0,10)
print(np.where(c < 2, c, c+1))

""" Is condition """
print(np.where(c == 3, "Talismar", c))

print(np.nan)