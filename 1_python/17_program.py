# map   
# The map() function applies a given function to all items in an input list (or any other iterable) and returns a map object (which is an iterator).
# Example 1: Using map() to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

#filter
# The filter() function constructs an iterator from elements of an iterable for which a function returns true.
# Example 2: Using filter() to get only even numbers from a list
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

# reduce
# The reduce() function is a part of the functools module and is used to apply a rolling
# computation to sequential pairs of values in a list. It reduces the list to a single value.
from functools import reduce
# Example 3: Using reduce() to calculate the product of all numbers in a list
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
