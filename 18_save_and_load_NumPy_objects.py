""" 
This section covers 
np.save
np.savez
np.savetxt
np.load
np.loadtxt
"""

""" 
 If you want to store a single ndarray object, store it as a .npy file using np.save.
 If you want to store more than one ndarray object in a single file, save it as a .npz 
 file using np.savez. You can also save several arrays into a single file in compressed 
 npz format with savez_compressed. 
"""

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

""" You can save it as “filename.npy” with: """

np.save("18_save", a)

""" You can use np.load() to reconstruct your array. """

print(np.load("18_save.npy"))

"""
You can save a NumPy array as a plain text file like a .csv or .txt file with np.savetxt 
"""

csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8,1,2,3,4,5])
#np.savetxt("18_new_file.csv", csv_arr, header="Array01", footer="Test to Talismar", comments="# This is array NumPy - ", delimiter=",")
np.savetxt("18_new_file.csv", csv_arr, header="Array01")


""" You can quickly and easily load your saved text file using loadtxt() """
print(np.loadtxt("18_new_file.csv"))


""" Importing and exporting a CSV """
import pandas as pd

x = pd.read_csv('18_new_file.csv',  header=0)
print(x.dtypes)

""" Plotting arrays with Matplotlib """
""" If you need to generate a plot for your values, it’s very simple with Matplotlib. """

import matplotlib.pyplot as plt

# plt.plot(x)
# plt.show()

""" For example, you can plot a 1D array like this """
x = np.linspace(0, 5, 20)
y = np.linspace(0, 10, 20)
plt.plot(x, y, 'purple') # line
plt.plot(x, y, 'o')      # dots

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
plt.show()