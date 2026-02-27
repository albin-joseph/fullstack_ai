# Sytax while loop
# while condition:
#     statement(s)  
# Example 1: Printing numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1  # Incrementing the value of i by 1  
    
# Example 2: Calculating the factorial of a number
num = 5
factorial = 1
while num > 1:
    factorial *= num  # factorial = factorial * num
    num -= 1  # Decrementing the value of num by 1
print(f"The factorial of 5 is {factorial}.")

# Example 3: Using while loop with else
count = 0
while count < 3:
    print(f"Count is {count}.")
    count += 1
else:
    print("Count has reached 3.")   