def count_word_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            print(f"Total words in the file: {word_count}")
            print(f"Total lines in the file: {len(lines)}")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        
count_word_lines("sample.txt")