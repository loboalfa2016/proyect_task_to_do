
def show_menu():
    print(f"""\n
      TO-DO PRO MENU
      1. Create New Task
      2. View Tasks
      3. Update Task
      4. Delete Task
      5. Filter Tasks
      6. Exit Menu
      """
      )
def start_menu():
    while True:
        show_menu()
        try:
            option = int(input("Choose what do you want to do: "))
            if option == 1:
                from service import add_task
                add_task()
            elif option == 2:
                from service import task_listing
                task_listing()
            elif option == 3:
                print("Update tasks Selected")
            elif option == 4:
                print("Delete task Selected")
            elif option == 5:
                from service import filter_tasks_by_status
                filter_tasks_by_status
            elif option == 6:
                print("Goodbye")
                break
            else:
                print("Invalid selection please type the number of the option you want (1-6): ")
        except ValueError:
            print("Something went wrong, please try again.")
