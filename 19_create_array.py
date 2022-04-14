import numpy as np

""" Generating random number repeating every time you run """
al = np.random.randint(1,10,10)
print(al)


""" Generating random number without repeat """
np.random.seed(32)
al = np.random.randint(1,10,10)
print(al)