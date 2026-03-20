Created menu:
Function defined as #start_menu will display the menu:
    TO-DO PRO MENU
      1. Create New Task
      2. View Tasks
      3. Update Task
      4. Delete Task
      5. Filter Tasks
      6. Exit Menu
The function "show_menu will execute in bucle the start_menu until user selects option #6. Exit Menu
  inside the bucle the number entered by the user will import and execute a function from service.py like this
    if option entered == 1
    will import: 'add_task()'
    will enable user to: Create task (Name the task, add a description, set a priority and tag it with a status)
    
    if option entered == 2
    will import: 'task_listing()'
    will enable user to: View existing Tasks
    
    if option entered == 3
    will import: 'update_task()'
    will enable user to: Update Task details. 

    if option entered == 4
    will import: delete_task()
    will enable user to: Remove a taskk from the existing tasks list

    if option entered == 5
    will import: filter_tasks_by_status
    will enable user to: Get the list of tasks that match with the entered option

    if option entered == 6
    will import: N/A
    will enable user to: Stop the program and exit the menu with a "Goodbye" message.