task = []

while True:
    print("\n1. Add Task\n2. Mark Task Complete\n3. View Tasks\n4. Delete Task\n5. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        add = input("Enter the task: ")
        task.append([add, False])
        print(f"Task '{add}' added!")

    elif choice == 2:
        if not task:
            print("No tasks to mark as complete.")
        else:
            print("\nYour tasks:")
            for i, t in enumerate(task):
                print(f"{i}. {t[0]} - {'Completed' if t[1] else 'Incomplete'}")

            mark = int(input("Enter the task number to mark as complete: "))
            if 0 <= mark < len(task):
                task[mark][1] = True
                print(f"Task '{task[mark][0]}' marked as complete!")
            else:
                print("Invalid task number!")

    elif choice == 3:
        if not task:
            print("No tasks yet!")
        else:
            for i, t in enumerate(task):
                print(f"{i}. {t[0]} - {'Completed' if t[1] else 'Incomplete'}")

    elif choice == 4:
        if not task:
            print("No tasks to delete.")
        else:
            print("\nYour tasks:")
            for i, t in enumerate(task):
                print(f"{i}. {t[0]} - {'Completed' if t[1] else 'Incomplete'}")

            delete = int(input("Enter the task number to delete: "))
            if 0 <= delete < len(task):
                deleted_task = task.pop(delete)
                print(f"Task '{deleted_task[0]}' deleted!")
            else:
                print("Invalid task number!")

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Please choose a valid option!")
