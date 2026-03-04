def append(filename, content):
    with open(filename, 'a') as file:
        file.write(content + '\n')

def read(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def write(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
