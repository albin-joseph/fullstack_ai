import numpy as np

# Array as scalar broadcasting
array = np.array([1, 2, 3])
scalar = 10
result = array + scalar  # Broadcasting the scalar to each element of the array    print("Result of adding scalar to array:", result)

matrix = np.array([[1, 2], [3, 4]])
scalar = 5
result_matrix = matrix * scalar  # Broadcasting the scalar to each element of the matrix
print("Result of multiplying scalar with matrix:\n", result_matrix)

vector = np.array([1, 2, 3])
matrix = np.array([[1, 2, 3], [4, 5, 6]])
result_vector_matrix = vector + matrix  # Broadcasting the vector to each row of the matrix
print("Result of adding vector to matrix:\n", result_vector_matrix)

 # Aggregation functions
array = np.array([1, 2, 3, 4, 5])
print("Sum of array:", np.sum(array))
print("Mean of array:", np.mean(array))
print("Standard deviation of array:", np.std(array))
matrix = np.array([[1, 2], [3, 4]])
print("Sum of matrix:", np.sum(matrix))
print("Mean of matrix:", np.mean(matrix))
print("Standard deviation of matrix:", np.std(matrix))
