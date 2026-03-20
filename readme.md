# Task Status Filter

## Description
This feature allows users to filter a list of tasks based on their status.  
It is useful for displaying only the tasks that match a specific state, such as *pending, **completed*, or any other status defined in the system.

The function processes a list of task objects (dictionaries) and returns only the tasks whose status matches the user-provided search value.

---

## Function Name
filter_tasks_by_status(tasks, search_status)

---

## Purpose
The purpose of this function is to:

- Receive a list of tasks
- Receive a status to search for
- Compare the status of each task with the provided value
- Return a new list containing only the matching tasks

This helps organize and display tasks more efficiently based on their current state.

---

## Parameters

### tasks (list)
A list of task dictionaries.  
Each task should contain a status key.

Example:
```python
[
    {"id": 1, "title": "Do homework", "status": "pending"},
    {"id": 2, "title": "Buy groceries", "status": "completed"}
]
