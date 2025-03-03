# Challenge_Day_07

tasks = []

def show_tasks():
    # Check if the tasks list is empty
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:\n")
        # Enumerate through the tasks list and print each task with its number
        for i, task in enumerate(tasks, 1):
            print(f"Task No : {i}. {task}")

def add_task():
    # Prompt user to enter a new task
    task = input("Enter a new task: ")
    # Add the new task to the tasks list
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    # Show current tasks before deletion
    show_tasks()
    try:
        # Prompt user to enter the task number to delete
        index = int(input("Enter task number to delete:")) - 1
        # Check if the entered index is valid
        if 0 <= index < len(tasks):
            # Remove the task at the specified index
            removed_task = tasks.pop(index)
            print(f"Deleted: {removed_task}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n-----To-Do List CLI-----\n")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit\n")

        # Prompt user to choose an option
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice, please try again.")

# Corrected the syntax error in the if statement
if __name__ == "__main__":
    main()