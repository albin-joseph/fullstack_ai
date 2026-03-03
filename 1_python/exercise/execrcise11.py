def read(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        
def write(file_name, content):
    try:
        with open(file_name, "w") as file:
            file.write(content)
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")

def append(file_name, content):
    try:
        with open(file_name, "a") as file:
            file.write(content)
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")  


while True:
    print("Choose an option:")
    print("1. Read a file")
    print("2. Write to a file")
    print("3. Append to a file")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        file_name = input("Enter the file name to read: ")
        read(file_name)
    elif choice == "2":
        file_name = input("Enter the file name to write to: ")
        content = input("Enter the content to write: ")
        write(file_name, content)
    elif choice == "3":
        file_name = input("Enter the file name to append to: ")
        content = input("Enter the content to append: ")
        append(file_name, "\n" + content)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")