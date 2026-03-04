import file_operations
while True:
    print("Welcome to the Task Manager!")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

    choice = input("Please enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task you want to add: ")
        file_operations.append('tasks.txt', task)
        print("Task added successfully!")
    elif choice == '2':
        print("Your tasks:")
        tasks = file_operations.read('tasks.txt')
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task.strip()}")
    elif choice == '3':
        print("Deleting a task")
        tasks = file_operations.read('tasks.txt')
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task.strip()}")
        task_number = int(input("Enter the task number to delete: "))
        if 0 < task_number <= len(tasks):
            del tasks[task_number - 1]
            file_operations.write('tasks.txt', '\n'.join(tasks))
            print("Task deleted successfully!")
    elif choice == '4':
        print("Exiting the Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")