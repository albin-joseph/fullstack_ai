numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Adding an element to the list

fruits = ["apple", "banana", "cherry"]
fruits.append("date")  # Adding an element to the list

mixed = [1, "apple", 3.14, True]
mixed.append("new element")  # Adding an element to the list

mixed.remove(3.14)  # Removing an element from the list

numbers[0] = 10  # Modifying an element in the list
fruits[1] = "blueberry"  # Modifying an element in the list

print(numbers)
print(fruits)
print(mixed)

print(numbers[0])  # Output: 1
print(fruits[1])  # Output: banana
print(mixed[2])   # Output: 3.14