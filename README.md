# IdeaJar

A terminal-based idea and task generator that pulls random activities based on your current energy level.

IdeaJar helps counter the clutter and inconvenience of physical jars or notebooks by keeping your tasks organized into digital "buckets" (e.g., low, medium, and high energy). It runs entirely locally on your machine, requiring no internet connection or external services.

## Prerequisites

Python 3 is required to run this program. You can download it from [python.org](https://www.python.org/downloads/).

On Ubuntu/Debian Linux, you can install it via the terminal:

    sudo apt update && sudo apt install python3

## How to Run

1. Open your terminal and navigate to the project directory:

    cd ~/workspace/ideajar

2. Start the program:

    python3 main.py

3. Enter the name of your jar file to load an existing collection or create a new one.

## Features & Usage

When the program starts, select an option by typing its corresponding number:

- [1] Pull idea: Select an energy level to randomly draw a task. After pulling, you can reroll, mark it as completed, or move it to your in-progress list.
- [2] Add or edit ideas: Add new tasks or remove existing tasks from any jar.
- [3] Edit energy levels: Customize your jars by adding new categories, renaming existing ones, or removing them.
- [4] Exit: Safely save your data and close the application.

Note: The `in_process` bucket is a reserved category used by the system to track active tasks and cannot be renamed or removed from within the menu.