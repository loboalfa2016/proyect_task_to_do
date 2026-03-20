#def delete_task():
#Defines the function responsible for deleting a task.

#if not selected_task:
#Checks if the task list is empty.

#print("No tasks to delete\n")
#Displays a message if there are no tasks.

#return
#Stops the function execution.

#task_listing()
#Shows the list of current tasks to the user.

#while True:
#Creates a loop to keep asking until valid input is given.

#try:
Attempts to execute code safely.

#i = int(input(...)) - 1
#Gets user input, converts it to an integer, and adjusts the index.

#if 0 <= i < len(selected_task):
#Validates that the input is within the valid range.

#selected_task.pop(i)
#Removes the selected task from the list.

#print("Task deleted\n")
#Confirms that the task was deleted.

#break
#Exits the loop after successful deletion.

#else:
#Handles invalid index values.

#print("Invalid number")
#Shows an error if the number is out of range.

#except ValueError:
#Catches errors when input is not a number.

#print("Error, enter a number\n")
#Displays an error message for invalid input.