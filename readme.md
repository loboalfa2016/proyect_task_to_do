#DELETE TASK

1. Check if the list is empty
if not selected_task:

Verifies if there are no tasks available

If empty, the function stops execution

print("No tasks to delete\n")
return
2. Show current tasks
task_listing()

Displays all tasks so the user can choose which one to delete

3. Start validation loop
while True:

Keeps asking the user until a valid input is provided

4. Get user input safely
i = int(input("\nEnter the task number to delete: ")) - 1

Requests a number from the user

Converts it to an integer

Subtracts 1 to match Python list indexing (starts at 0)

5. Validate the input range
if 0 <= i < len(selected_task):

Ensures the number is within the valid range of the list

Prevents errors like "index out of range"

6. Delete the task
selected_task.pop(i)

Removes the task at the selected position

print("Task deleted\n")

Confirms the deletion

break

Exits the loop after successful deletion

7. Handle invalid numbers
else:
    print("Invalid number")

Displays an error if the number does not exist

8. Handle invalid input (letters, symbols)
except ValueError:
    print("Error, enter a number\n")

Prevents the program from crashing if the user enters non-numeric values
##  Core Functions
# Core Functions

###  Description
This project includes three main functionalities: validating input data, adding tasks, and updating existing tasks. These functions work together to ensure correct task management.

---

##  Validation Functions

These functions are used to verify that the user input is valid before saving or updating tasks.

### validate_title(title)
## Validation Functions

These functions are used to verify that the user input is valid before saving or updating tasks.

###  validate_title(title)
Checks that the task title is not empty.

###  validate_description(description)
Checks that the task description is not empty.

###  validate_priority(priority)
Checks that the priority is valid (`high`, `mid`, `low`).  
This validation is case-insensitive.

---

##  add_task()
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

###  Description
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

##  Example Workflow
## Example Workflow

1. Add a task  
2. View the task list  
3. Update a task  
4. Validate inputs before saving changes
