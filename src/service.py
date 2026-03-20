import valiadation

selected_task = []

def add_task():
    title = input("Enter the TASK name: ")
    description = input("Enter the TASK description: ")
    priority = input("Enter the TASK priority (high, mid, low): ")

    print("\nSelect the Task status :")
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
            print("error")
            status = 'Pending'
    if valiadation.validate_title(title) and valiadation.validate_description(description) and valiadation.validate_priority(priority):
        task_data ={
            "title": title,
            "description": description,
            "priority": priority,
            "status": status
        } 
        selected_task.append(task_data)
    else:
        print("error")


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
            print(f'task #{i} \n NAME: {j["title"]} \n STATUS: {j["status"]} \n PRIORITY: {j["priority"]} \n')
    else:
        print("empty list")


def update_task():
    if selected_task:
        task_listing()
        try:
            indice = int(input("Enter the task # to update: ")) - 1
            if 0 <= indice < len(selected_task):
                task_selected = selected_task[indice]
                print("\nEnter the new task information (leave blank to stop making changes): ")
                title = input(f"Title ({task_selected['title']}): ")
                description = input(f"Description ({task_selected['description']}): ")
                priority = input(f"Priority ({task_selected['priority']}): ")
                
                print("\nSelecct the task's new status: ")
                print("1. Pending")
                print("2. In Progress")
                print("3. Completed")
                status_option = input("Enter the new task status (leave blank to stop making changes): ")

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
                print("Task successfuly updated!")
            else:
                print("Invalid Index.")
        except ValueError:
            print("Invalid Index.")
    else:
        print("No tasks.")


def delete_task():
    if not selected_task:
        print("No tasks to delete\n")
        return

    task_listing() 

    while True: 
        try:  
            i = int(input("\nEnter the task number to delete: ")) -1 

            if 0 <= i < len(selected_task):
                selected_task.pop(i)
                print("Task deleted\n")
                break
            else:
                print("Invalid number")

        except ValueError:
            print("Error, enter a number\n") 
            


