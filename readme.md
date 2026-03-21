# TO-DO PRO 📝

A simple task manager developed in Python for the command line.

## Description
**TO-DO PRO** is a program that allows you to manage your tasks efficiently. You can create, list, update, and delete tasks, as well as filter them by their current status.

## Features
* **Create:** Add new tasks with title, description, priority, and status.  
* **List:** View all registered tasks with their details.  
* **Update:** Modify the details of an existing task.  
* **Delete:** Remove tasks from the list.  
* **Filter:** Search for specific tasks based on their status.  

## Project Structure
The project is divided into three main files:
* `menu.py`: Handles the menu logic and user interaction.  
* `services.py`: Contains task management and storage functions.  
* `main.py`: Entry point that starts the program execution.  

## Requirements
* **Python 3.10** or higher (required for `match` statement support).

## Execution
1. Clone the repository to your local machine.  
2. Open a terminal in the project folder.  
3. Run the following command:
   ```bash
   python main.py
   ```

## Usage
1. Start the program.  
2. Select an option from the main menu by entering the corresponding number.  
3. Follow the instructions in the console to complete the desired action.  

---

## Project Code

### 1. `menu.py`
```python
def start_menu():
    print("\n--- TO-DO PRO MENU ---")
    print("1. Create New Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Filter Tasks")
    print("6. Exit Menu")

def show_menu():
    import services
    while True:
        start_menu()
        option = input("Enter your choice: ")
        match option:
            case "1":
                services.add_task()
            case "2":
                services.task_listing()
            case "3":
                services.update_task()
            case "4":
                services.delete_task()
            case "5":
                services.filter_tasks_by_status()
            case "6":
                print("Goodbye!")
                break
            case _:
                print("Invalid option. Please try again.")
```

### 2. `services.py`
```python
import valiadation

selected_task = []

def add_task():
    title = input("Enter the TASK name: ")
    description = input("Enter the TASK description: ")
    priority = input("Enter the TASK priority (high, mid, low): ")

    print("\nSelect the task status:")
    print("1. Pending")
    print("2. In Progress")
    print("3. Completed")
    status_option = input("Enter an option: ")

    match status_option:
        case "1":
            status = 'Pending'
        case "2": 
            status = 'In Progress'
        case "3": 
            status = 'Completed'
        case _:
            print("Error")
            status = 'Pending'

    if valiadation.validate_title(title) and valiadation.validate_description(description) and valiadation.validate_priority(priority):
        task_data = {
            "title": title,
            "description": description,
            "priority": priority,
            "status": status
        } 
        selected_task.append(task_data)
    else:
        print("Error")


def filter_tasks_by_status(tasks, search_status):
    """
    Filters tasks based on the provided status.
    
    Parameters:
        tasks (list): list of tasks (dictionaries)
        search_status (str): status to filter by
    
    Returns:
        list: list of tasks that match the status
    """
    if not tasks:
        return []

    search_status = search_status.strip().lower()

    filtered_tasks = [
        task for task in tasks
        if task.get("status", "").strip().lower() == search_status
    ]

    return filtered_tasks


def task_listing():
    if len(selected_task) > 0:
        for i, j in enumerate(selected_task, start=1):
            print(f'Task #{i} \n NAME: {j["title"]} \n STATUS: {j["status"]} \n PRIORITY: {j["priority"]} \n')
    else:
        print("Empty list")


def update_task():
    if selected_task:
        task_listing()
        try:
            index = int(input("Enter the task # to update: ")) - 1
            if 0 <= index < len(selected_task):
                task_selected = selected_task[index]
                print("\nEnter the new task information (leave blank to keep current values):")
                title = input(f"Title ({task_selected['title']}): ")
                description = input(f"Description ({task_selected['description']}): ")
                priority = input(f"Priority ({task_selected['priority']}): ")
                
                print("\nSelect the new task status:")
                print("1. Pending")
                print("2. In Progress")
                print("3. Completed")
                status_option = input("Enter the new task status (leave blank to keep current): ")

                if title:
                    task_selected['title'] = title
                if description:
                    task_selected['description'] = description
                if priority:
                    if valiadation.validate_priority(priority):
                        task_selected['priority'] = priority
                    else:
                        print("Invalid priority. Not changed.")
                if status_option:
                    match status_option:
                        case "1":
                            task_selected['status'] = "Pending"
                        case "2":
                            task_selected['status'] = "In Progress"
                        case "3":
                            task_selected['status'] = "Completed"
                        case _:
                            print("Invalid option. Not changed.")

                print("Task successfully updated!")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid index.")
    else:
        print("No tasks.")


def delete_task():
    if not selected_task:
        print("No tasks to delete\n")
        return

    task_listing() 

    while True: 
        try:  
            i = int(input("\nEnter the task number to delete: ")) - 1 

            if 0 <= i < len(selected_task):
                selected_task.pop(i)
                print("Task deleted\n")
                break
            else:
                print("Invalid number")

        except ValueError:
            print("Error, enter a number\n")
```

### 3. `validation.py`
```python
def validate_title(title):
    return len(title) > 0

def validate_description(description):
    return len(description) > 0

def validate_priority(priority):
    return priority.lower() in ["high", "mid", "low"]
```

### 4. `main.py`
```python
from menu import start_menu

if __name__ == "__main__":
    start_menu()
```
