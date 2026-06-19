# To-Do List Manager

A simple text-based To-Do List application written in Python for my Introduction to Python mini-project. The program allows users to create and manage tasks, save them to a file, and load them when the program is run again. Users can also have the program randomly select a task to work on.

## How to Use

1. Make sure Python 3 is installed.
2. Download or clone the project files.
3. Open a terminal in the project folder.
4. Run the program:

python main.py

5. Use the menu to:

   * Add tasks
   * View tasks
   * Pick a random task
   * Quit the program

## Files

| File      | Purpose                                                              |
| --------- | -------------------------------------------------------------------- |
| main.py   | The main program file.                                               |
| tasks.txt | Stores the user's tasks. Created automatically when tasks are saved. |

## Python Concepts Demonstrated

### Meaningful Comments

The code includes comments that explain the purpose of important sections and functions.

### Lists

Tasks are stored in a Python list while the program is running.

### Loops

A while loop keeps the menu running until the user chooses to quit. For loops are used when displaying and saving tasks.

### User-Defined Functions

Functions are used to organize the program into smaller pieces such as loading tasks, saving tasks, and displaying tasks.

### File Read/Write

Tasks are saved to and loaded from a text file so that information is preserved between sessions.

### Random Number Generation

The program uses Python's random module to randomly select a task for the user.

## Author

Charmae Edge
