import pickle
import os

# Define the file where the to-do list will be saved
TODO_FILE = 'todo_list.pkl'

# Load the to-do list from file if it exists
def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'rb') as file:
            return pickle.load(file)
    return []

# Save the to-do list to file
def save_todo_list(todo_list):
    with open(TODO_FILE, 'wb') as file:
        pickle.dump(todo_list, file)

# Add a new task to the to-do list
def add_task(todo_list, task_description):
    todo_list.append({'task': task_description, 'completed': False})
    save_todo_list(todo_list)
    print(f"Task '{task_description}' added successfully.")

# Display all tasks in the to-do list
def view_tasks(todo_list):
    if not todo_list:
        print("No tasks found.")
        return

    print("\nYour To-Do List:")
    for index, task in enumerate(todo_list, start=1):
        status = "✓" if task['completed'] else "✗"
        print(f"{index}. {task['task']} - [{status}]")

# Mark a task as completed
def complete_task(todo_list, task_number):
    if 1 <= task_number <= len(todo_list):
        todo_list[task_number - 1]['completed'] = True
        save_todo_list(todo_list)
        print(f"Task '{todo_list[task_number - 1]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

# Update a task description
def update_task(todo_list, task_number, new_description):
    if 1 <= task_number <= len(todo_list):
        old_task = todo_list[task_number - 1]['task']
        todo_list[task_number - 1]['task'] = new_description
        save_todo_list(todo_list)
        print(f"Task '{old_task}' updated to '{new_description}'.")
    else:
        print("Invalid task number.")

# Delete a task from the to-do list
def delete_task(todo_list, task_number):
    if 1 <= task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        save_todo_list(todo_list)
        print(f"Task '{removed_task['task']}' deleted.")
    else:
        print("Invalid task number.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\nTo-Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            view_tasks(todo_list)
        elif choice == '2':
            task_description = input("Enter the task description: ").strip()
            add_task(todo_list, task_description)
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as completed: "))
            complete_task(todo_list, task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to update: "))
            new_description = input("Enter the new task description: ").strip()
            update_task(todo_list, task_number, new_description)
        elif choice == '5':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(todo_list, task_number)
        elif choice == '6':
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
