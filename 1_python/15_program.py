# python list comprehensions
# list comprehensions are a concise way to create lists
# they consist of brackets containing an expression followed by a for clause, then zero or more for or if clauses
# the expressions can be anything, meaning you can put in all kinds of objects in lists
# the result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it

# example 1: create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)

# example 2: create a list of even numbers from 0 to 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# example 3: create a list of tuples containing numbers and their squares from 0 to 9
squares_tuples = [(x, x**2) for x in range(10)]
print(squares_tuples)