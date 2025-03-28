This program is a To-Do List Manager that allows users to manage tasks. Here's a brief summary of its features:

Task Management:

The program stores tasks in a file (tasks.txt) and supports various actions such as adding, editing, viewing, deleting, and marking tasks as completed.

Functions:

Load Tasks: Reads the tasks from the file into a list when the program starts.

Save Tasks: Writes the updated list of tasks to the file after any changes.

Add Task: Prompts the user to input a task description and deadline, and then adds it to the task list.

View Tasks: Displays all tasks, separated into "Pending" and "Completed" categories.

Edit Task: Allows the user to modify an existing task's description and deadline.

Delete Task: Deletes a specific task by its ID.

Mark as Completed: Changes the status of a task to "Completed."

Display Menu: Shows the main menu with options to add, view, edit, delete, mark as completed, or exit the program.

Main Program Loop: The program keeps running in a loop, displaying the menu and responding to user inputs until the user chooses to exit.

This program helps users organize their tasks and keeps track of their progress using a simple text-based interface.




Here's a brief summary of its features:

Task Management:

The program stores tasks in a file (tasks.txt) and supports various actions such as adding, editing, viewing, deleting, and marking tasks as completed.

Functions:

Load Tasks: Reads the tasks from the file into a list when the program starts.

Save Tasks: Writes the updated list of tasks to the file after any changes.

Add Task: Prompts the user to input a task description and deadline, and then adds it to the task list.

View Tasks: Displays all tasks, separated into "Pending" and "Completed" categories.

Edit Task: Allows the user to modify an existing task's description and deadline.

Delete Task: Deletes a specific task by its ID.

Mark as Completed: Changes the status of a task to "Completed."

Display Menu: Shows the main menu with options to add, view, edit, delete, mark as completed, or exit the program.

Main Program Loop: The program keeps running in a loop, displaying the menu and responding to user inputs until the user chooses to exit.







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
