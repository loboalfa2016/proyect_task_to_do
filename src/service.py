
def list_tasks():
    task = []
    option = -1
    if option == 3:
        if len(task) > 0:
            for i, j in enumerate(task, start=1):
                print(f'task #{i + 1} . NAME:{j['name']} STATE: {j['state']} PRIORITY: {j['priority']} \n')
        else:
            print("empty list")