import numpy as np

arr = np.array([1,2,3,4,5])
print(arr[0:])
print(arr[-2:])
print(arr[arr < 5])

a = np.array([[11 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a > 8])

""" 
You can also select, for example, numbers that are equal to or greater than 5,
and use that condition to index an array.
"""
five_up = (a >= 4)
print(a[five_up])

""" You can select elements that are divisible by 2 """

divisible_by_2 = a[a%2==0]
print(divisible_by_2)

""" Or you can select elements that satisfy two conditions using the & and | operators """
c = a[(a > 2) & (a < 11)]
print(c)

five_up = (a > 5) | (a == 5)
print(five_up)


""" Select elements or indices from an array """
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

b = np.nonzero(a == 1)
list_of_coordinates= list(zip(b[0], b[1]))

for coord in list_of_coordinates:
    print(coord)