task = []
option = -1
if option == 3:
    print("the task list is: \n")
    if len(task) > 0:
        for i, j in enumerate(task):
            print(f'task #{i + 1} . NAME:{j["name"]} STATE: {j["state"]} PRIORITY: {j["priority"]} \n')
    else:
        print("empty list")
