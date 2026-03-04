## Week 1: Python Programming Basics

- **Day 1**: Introduction to Python Development Setup
    - Install python
    - Setting up a coding environment
        - Install jupyter Notebook
            - pip install jupyter
        - Install visual studio code
- **Day 2**: Control Flow in Python
    - **if**
        - if: Executes code if the condition is true
        - elif: Add additional consitions after the initial if
        - else: Executes code if none of the previous consitions are met
    - *Loops*:
        - for Loops
            - Iterate over a sequence
        - while loops
            - exwecute still the condition meet
    - *break*:
        - Terminated the loop prematurely when a condition is met
    - *continue*:
        - Skip the current iteration and will continue to the next loop

- **Day 3**: Functions and Modules
    - **Function**
        - def keyword use for create a function
        - def <function_name>(<parameters>):
            #code block
            return <result>
        - Scope: 
            - local scope: only inside the block or function
            - global scope: out side function defined available globaly
        - Lifetime:
            - local scope variable not available after function execution, but global availble still program exists
    - **Modules**:
        - Modules are python files contian collection of functions and variables that can be reuse
        - Import
            - entire module
            - specific function
            - Use aliases
        - Creating Custom Modules
- **Day 4**: Data Structures(Lists, Tuples, Dictionaries, Sets)
    - Lists:
        - List are ordered mutable collections
        - Access elements by index
        - Slicing, pop, insert, del, remove
    - Tuples:
        - Immutable collection of items
    - Dictionaries:
        - Key value pair collections to easy to look up
    - Sets:
        - Unordered collection of unique items
- **Day 5**: Working with Strings
    - Concatenation
    - slicing
    - formatting
    - split
    - join
    - replce
- **Day 6**: File handling
    - Open files: r|w|a|+r
    - Reading Files: read()|readline()|readlines()
- **Day 7**: Python code and project
    - **python list comprehensions**
        - list comprehensions are a concise way to create lists
        - they consist of brackets containing an expression followed by a for clause, then zero or more for or if clauses
        -  the expressions can be anything, meaning you can put in all kinds of objects in lists
        -  the result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it
    - **Lambda Function**
        - Lambda functions are anonymous functions that can be defined in a single line of code. They are often used for short, simple functions that are not worth defining with a full function definition.
        - The syntax for a lambda function is as follows: lambda arguments: expression


[Back](../README.md)