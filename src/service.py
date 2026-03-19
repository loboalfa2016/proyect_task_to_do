task = {}

for i, j in enumerate(task, start=1):
    print(f'task #{i + 1} . NAME:{j['name']} STATE: {j['state']} PRIORITY: {j['priority']} \n')
else:
    print('empty list')
    break