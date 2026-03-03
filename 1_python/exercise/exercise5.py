
arr = []
for i in range(10):
    arr.append(number := int(input("Enter a number: ")))
    
print("Numbers entered: ", arr)
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num
print("The largest number is: ", largest)
