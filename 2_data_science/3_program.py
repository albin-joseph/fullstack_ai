import numpy as np

arr = np.array([10,20,30,40,50, 60])
print(arr[2])
print(arr[-1])
print(arr[1:4])
print(arr[:3])
print(arr[2:])

reshaped_arr = arr.reshape(2,3)
print("Reshaped Array (2x3):\n", reshaped_arr)
