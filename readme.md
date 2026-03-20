# Core Functions

###  Description
This project includes three main functionalities: validating input data, adding tasks, and updating existing tasks. These functions work together to ensure correct task management.

---

## Validation Functions

These functions are used to verify that the user input is valid before saving or updating tasks.

### 🔤 validate_title(title)
Checks that the task title is not empty.

### 📝 validate_description(description)
Checks that the task description is not empty.

### ⚡ validate_priority(priority)
Checks that the priority is valid (`high`, `mid`, `low`).  
This validation is case-insensitive.

---

## add_task()

###  Description
This function allows the user to create a new task by entering its information.

###  How it works
- The user enters title, description, and priority.
- The user selects a status (Pending, In Progress, Completed).
- The data is validated using validation functions.
- If valid, the task is stored in a list.
- If not valid, an error message is shown.

---

## update_task()

### Description
This function allows the user to modify an existing task.

###  How it works
- Displays the list of tasks.
- The user selects a task by its number.
- The user can update:
  - Title
  - Description
  - Priority
  - Status
- If a field is left blank, the current value is kept.
- Only valid data is updated.

---

##  Notes
- Tasks are stored in a list of dictionaries.
- Input validation helps prevent errors.
- The system allows partial updates without overwriting all data.

---

## Example Workflow

1. Add a task  
2. View the task list  
3. Update a task  
4. Validate inputs before saving changes
