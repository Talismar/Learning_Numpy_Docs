""" 
This section covers np.unique()
"""
"uniques - exclusivos"

import numpy as np

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
print(np.unique(a))

""" To get the indices of unique values in a NumPy array """
print(np.unique(a, return_index=True)[1])

""" 
You can pass the return_counts argument in np.unique()
along with your array to get the frequency count of unique values in a NumPy array.
"""
unique_values, occurrence_count = np.unique(a, return_counts=True)
print(occurrence_count)
# print(np.unique(a,return_counts=True)[1])

""" You can find unique values with """
""" If the axis argument isn’t passed, your 2D array will be flattened. """
a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
unique_values = np.unique(a_2d)
print(unique_values)

""" 
If you want to get the unique rows or columns, make sure to pass the axis argument.
To find the unique rows, specify axis=0 and for columns, specify axis=1.
"""
unique_rows = np.unique(a_2d, axis=0)
# print(unique_rows)

unique_rows, indices, occurrence_count = np.unique(
     a_2d, axis=0, return_counts=True, return_index=True)
print(unique_rows)
print(indices)
print(occurrence_count)