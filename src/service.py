import valiadation

task = []

def add_task():
    title = input("Enter the TASK name: ")
    description = input("Enter the TASK description: ")
    priority = input("Enter the TASK priority (high, mid, low)")

    print("\nSelect the Task status :")
    print("1. Pending")
    print("2. In Progress")
    print("3. Completed")
    status_option = input("Enter an option: ")

    match status_option:
        case 1:
            status = 'Pending'
        case 2: 
            status = 'In Progress'
        case 3: 
            status = 'Completed'
        case _:
            print("error")
            status = 'Pending'
    if valiadation.validate_title(title) and valiadation.validate_description(description) and valiadation.validate_priority(priority):
        tasks ={
            "title": title,
            "description": description,
            "priority": priority,
            "status": status
        } 
        task.append(tasks)
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

task = []
def task_listing():
    option = -1
    if option == 3:
        print("the task list is: \n")
    if len(task) > 0:
        for i, j in enumerate(task, start=1):
            print(f'task #{i + 1} . NAME:{j["name"]} STATE: {j["state"]} PRIORITY: {j["priority"]} \n')
    else:
        print("empty list")


def update_task():
    if task:
        task_listing()
        try:
            indice = int(input("Enter the task # to update: ")) - 1
            if 0 <= indice < len(task):
                task = task[indice]
                print("\nEnter the new task information (leave blank to stop making changes): ")
                title = input(f"Title ({task['title']}): ")
                description = input(f"Description ({task['description']}): ")
                priority = input(f"Priority ({task['priority']}): ")
                
                print("\nSelecct the task's new status: ")
                print("1. Pending")
                print("2. In Progress")
                print("3. Completed")
                status_option = input("Enter the new task status (leave blank to stop making changes): ")

                if title:
                    task['title'] = title
                if description:
                    task['description'] = description
                if priority:
                    if valiadation.validar_prioridad(priority):
                        task['priority'] = priority
                    else:
                        print("Invalid priority. Not changed.")
                if status_option:
                    match status_option:
                        case "1":
                            task['status'] = "pending"
                        case "2":
                            task['status'] = "in progress"
                        case "3":
                            task['status'] = "completed"
                        case _:
                            print("Invalid option. Not changed.")
                print("Task successfuly updated!")
            else:
                print("Invalid Index.")
        except ValueError:
            print("Invalid Index.")
    else:
        print("No tasks.")

