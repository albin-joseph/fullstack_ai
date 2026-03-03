while True:
    str = input("Enter a string: ")
    if str == "exit":
        print("Exiting the program.")
        break
    leng = len(str)
    is_palindrome = False
    print("Length of the string is:", leng)
    for i in range(leng // 2):
        if(str[i] != str[leng - i - 1]):
            is_palindrome = False
            print("The string is not a palindrome.")
            break
        else:   
            is_palindrome = True
    if(is_palindrome):
        print("The string is a palindrome.")