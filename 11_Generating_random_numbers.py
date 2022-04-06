""" You can generate a 2 x 4 array of random integers between 0 and 4 with """
# Do this (new version)
from numpy.random import default_rng
rng = default_rng()
# print(rng.integers(5, size=(2, 4)))

vals = rng.standard_normal(10)
print(vals)