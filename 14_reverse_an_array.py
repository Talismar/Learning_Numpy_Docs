""" This section covers np.flip() """

""" Reversing a 1D array """
""" If you begin with a 1D array like this one """

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(np.flip(arr))

""" Reversing a 2D array """

arr_2d = np.array([arr, [9,10,11,12,13,14,15,16]])
# print(np.flip(arr_2d))

""" You can easily reverse only the rows with """
reversed_arr_rows = np.flip(arr_2d, axis=0)
# print(reversed_arr_rows)

""" Or reverse only the columns with """
reversed_arr_columns = np.flip(arr_2d, axis=1)
# print(reversed_arr_columns)

""" You can also reverse the contents of only one column or row.  """
arr_2d[1] = np.flip(arr_2d[1])
# print(arr_2d)

""" You can also reverse the column at index position 1 (the second column) """
arr_2d[:,2] = np.flip(arr_2d[:,2])
print(arr_2d)

