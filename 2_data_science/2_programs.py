import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

# Reshape the array to 5x1
reshaped_arr = arr.reshape(5, 1)
print("Reshaped Array (5x1):\n", reshaped_arr)

a = np.array([1,2,3])
b = np.array([4,5,6])

print("Array a:", a)
print("Array b:", b)    

print("Element-wise addition:", a + b)
print("Element-wise multiplication:", a * b)   

arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Square Root:", np.sqrt(arr)) 
print("Exponential:", np.exp(arr))
print("Max:", np.max(arr))