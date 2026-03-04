# Lambda functions are anonymous functions that can be defined in a single line of code. They are often used for short, simple functions that are not worth defining with a full function definition.
# The syntax for a lambda function is as follows:
# lambda arguments: expression
# Example 1: A lambda function that adds two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8   
# Example 2: A lambda function that squares a number
square = lambda x: x ** 2
print(square(4))  # Output: 16
# Example 3: A lambda function that checks if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(10))  # Output: True
print(is_even(7))   # Output: False 

