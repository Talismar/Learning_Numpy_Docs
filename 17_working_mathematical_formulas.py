""" MeanSquareError """
""" 
In this example, both the predictions and labels vectors contain three values,
meaning n has a value of three. After we carry out subtractions the 
values in the vector are squared. 
"""

import numpy as np

error = np.square(np.array([1,1,1]) - np.array([1,2,3]))
print(error)

error = (1/3) * np.sum(np.square(np.array([1,1,1]) - np.array([1,2,3])))
print(error)