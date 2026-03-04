# NumPy is a powerful library for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.    
import numpy as np
# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)    

# Using built-in functions to perform operations on arrays

zeros = np.zeros((3,3))  # Create a 3x3 array of zeros
print("Zeros Array:\n", zeros)

range_array = np.arange(0, 10, 2)  # Create an array of even numbers from 0 to 10
print("Range Array:", range_array)

linespace_array = np.linspace(0, 1, 5)  # Create an array of 5 evenly spaced numbers between 0 and 1
print("Linspace Array:", linespace_array)