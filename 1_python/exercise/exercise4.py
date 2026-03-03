# calculator program

result = 0.0
while True:
    print("Current result: ", result)
    user_input = input("Enter an operation and a number (e.g. + 5), or 'exit' to quit: ")
    
    if user_input.lower() == 'exit':
        print("Exiting the calculator. Final result: ", result)
        break
    
    try:
        operation, number = user_input.split()
        number = float(number)
        
        if operation == '+':
            result += number
        elif operation == '-':
            result -= number
        elif operation == '*':
            result *= number
        elif operation == '/':
            if number != 0:
                result /= number
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please use +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter an operation followed by a number.")