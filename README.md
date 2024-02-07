
Project Description:

This project marks the initial phase of the AirBnB clone development. It focuses on the backend construction, interfacing it with a console application using Python's cmd module.

Data, represented as Python objects, are serialized and stored in a JSON file. The JSON module in Python facilitates easy access to this stored data.

Description of the Command Interpreter:

The command-line interface resembles the Bash shell, but it only accepts a limited set of commands tailored for the AirBnB website.

This command-line interpreter acts as the front-end of the web app, allowing users to interact with the Python OOP backend.

Key commands include:

show
create
update
destroy
count
The command line interpreter, coupled with the backend and file storage system, supports various actions such as:

Creating new objects (e.g., User, Place)
Retrieving objects from storage
Performing operations on objects (e.g., counting, computing stats)
Updating object attributes
Deleting objects
How to Start It:

Follow these steps to set up and run the project on your local Linux machine for development and testing purposes:

Installing:

Clone the project repository from Github, which contains the console program and its dependencies:

bash
Copy code
git clone https://github.com/Tasnimsomo/AirBnB_clone.git
After cloning, navigate to the "AirBnB_clone" directory, where you'll find various files necessary for the program's functionality.

How to Use It:

The program operates in two modes:

Interactive Mode: User inputs commands directly into the console, following the provided prompts.
Non-Interactive Mode: Commands are piped into the console's execution.
Format of Command Input:

Commands should be separated by spaces. In non-interactive mode, use the echo command for piping.

Arguments:

Most commands accept options or arguments, which should be separated by spaces. For example:

bash
Copy code
./console.py create BaseModel
Available Commands:

The interpreter recognizes the following commands and their functionalities:

quit or EOF: Exits the program.

help: Provides usage instructions for a specific command or lists available commands.

create: Creates a new instance of a valid class, saves it to the JSON file, and prints the ID.

show: Prints the string representation of an instance based on the class name and ID.

destroy: Deletes an instance based on the class name and ID, saving changes to the JSON file.

all: Prints string representations of all instances based on the class name or all instances.

update: Updates an instance based on the class name and ID by adding or updating an attribute, saving changes to the JSON file.

count: Retrieves the number of instances of a class.

These commands facilitate interaction with the AirBnB clone project, allowing users to manage data effectively through the console interface.
