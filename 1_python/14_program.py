try:
    with open("./sample.txt", "r") as file:
        content = file.readlines()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
    
with open("sample.txt", "w") as file:
    file.write("This is a sample text file.\nIt has multiple lines.\n") 

with open("sample.txt", "a") as file:
    file.write("This line is appended to the file.\n")

