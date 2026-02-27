# Example: Checking if a number is even or odd

num = 0
if num > 0:
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
else:
    print("Please enter a positive number.")
    
# Example: Finding the number is +ve, negative or zero

if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:   
    print(f"{num} is zero.")