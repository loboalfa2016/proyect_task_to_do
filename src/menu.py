validation = -1
while validation != 0:
    print('welcome To-Do Pro')
    options = {'1': 'Add Task', '2': 'View Tasks', '3': 'Edit Task', '4': 'Delete Task', '5': 'Filter Tasks by Status', '0': 'Exit'}
    for key, value in options.items():
        print(f"{key} - - {value} - - ")
    validation = int(input("Enter your choice: "))