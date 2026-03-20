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