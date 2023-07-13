AirBnB clone - The console

Description:
	This team project is part of the Holberton School Full-Stack Software Engineer program. It's the first step towards building our first full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management and the base classes for thestorage of this data.

Usage:
	Our console works in interactive mode and non-interactive mode, like a Unix shell.

It prints the prompt (hbnb) and waits for the user for input.

Commands:
Run the console:	./console.py
Quit the console:	(hbnb) quit
Display the help for a command:	(hbnb) help <command>
Create an object (prints its id):	(hbnb) create <class>
Show an object:	(hbnb) show <class> <id> or (hbnb) <class>.show(<id>)
Destroy an object:	(hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)
Show all objects, or all instances of a class:	(hbnb) all or (hbnb) all <class>
Update an attribute of an object	(hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")
Count the number of instances of an object:	(hbnb) <class>.count()
Update attributes of an object using an dictionary:	(hbnb) <class>.update("<id>", {dictionary representation})

Note: For updating attributes using a dictionary representation:

The class ID must be in double quotes in order for the dictionary to be parsed correctly
If the attribute value is a string, use the format: 'key': "value"
If the attribute value is a number, use the format: "key": value
Non-interactive mode example
