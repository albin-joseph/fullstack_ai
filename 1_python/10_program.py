student = {
        "name": "Alice",
        "age": 20,
        "courses": ["Math", "Science", "History"],
        "grade": "A"}

print(student["name"])
print(student["age"])

student["grade"] = "A+"
print(student)

del student["age"]
print(student)
    
student.pop("courses")
print(student)

for key in student:
    print(key, student[key])

student.clear()
print(student)