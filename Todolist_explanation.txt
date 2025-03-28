File Handling:

The tasks are stored in tasks.txt in the format: Task ID, Description, Deadline, Status.

The load_tasks function reads the file and loads the tasks into a list.

The save_tasks function writes the tasks back to the file.


Task Operations:

Add Task: Prompts the user to enter a description and deadline, assigns a new ID, and saves the task.

View Tasks: Displays all pending and completed tasks.

Edit Task: Allows the user to modify the description and deadline of an existing task.

Delete Task: Removes a task based on its ID.

Mark Task as Completed: Changes the task's status to "Completed".


Menu Interface:

The user is presented with a simple menu to choose between the different actions (add, view, edit, delete, mark as completed, or exit).

The program loops until the user chooses to exit.


Welcome to To-Do List Manager!
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Mark Task as Completed
6. Exit

