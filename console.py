#!/usr/bin/python3
"""Implementation of a cmd Module"""
import cmd
import json
import shlex
import re
from models.engine.file_storage import FileStorage

classes = {'BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review'}


def get_content(args):
    """Returns the '(<content>)' from a given string
    """
    return args[args.rfind("(") + 1:args.rfind(")")]


class HBNBCommand(cmd.Cmd):
    """Class that implements the HolbertonBnb cmd

    Args:
        prompt ([str]): [Prompt to show]

    Returns:
        [type]: [infinite loop]
    """
    prompt = "(hbnb) "

    def do_create(self, args):
        """creates an instance of a given class, saves it to a JSON file"""
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        obj = eval(args[0])()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """method retrieves and prints the string
        representation of an instance based on the class name and ID."""
        inputs = shlex.split(args)
        if not inputs:
            print('** class name missing **')
        elif inputs[0] not in classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        elif '{}.{}'.format(inputs[0], inputs[1]) not in FileStorage.all(self):
            print("** no instance found **")
        else:
            key = '{}.{}'.format(inputs[0], inputs[1])
            content = FileStorage.all(self)[key]
            print(content)

    def do_destroy(self, args):
        """method deletes an instance
        based on its ID."""
        inputs = shlex.split(args)
        if not inputs:
            print('** class name missing **')
        elif inputs[0] not in classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        elif '{}.{}'.format(inputs[0], inputs[1]) not in FileStorage.all(self):
            print("** no instance found **")
        else:
            key = '{}.{}'.format(inputs[0], inputs[1])
            del FileStorage.all(self)[key]
            FileStorage.save(self)

    def do_all(self, args):
        """ prints the string
        representation of all instances of a given
         class or all instances in general."""
        args = shlex.split(args)
        dict_1 = FileStorage.all(self)

        if not args:
            print([str(value) for value in dict_1.values()])
            return
        if args[0] in classes:
            print([str(value) for key, value in dict_1.items()
                   if key.split(".")[0] == args[0]])
            return
        print("** class doesn't exist **")

    def do_update(self, args):
        """ method updates an instance based on the class name,
         ID, attribute name, and new value.
        """

        integers = {'number_rooms', 'number_bathrooms',
                    'max_guest', 'price_by_night'}
        floats = {'latitude', 'longitude'}
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if '{}.{}'.format(args[0], args[1]) not in FileStorage.all(self):
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        if args[2] in floats:
            try:
                args[3] = float(args[3])
            except ValueError:
                args[3] = 0.0
        if args[2] in integers:
            try:
                args[3] = int(args[3])
            except ValueError:
                args[3] = 0
        content = FileStorage.all(self)['{}.{}'.format(args[0], args[1])]
        setattr(content, args[2], args[3])
        content.save()

    def emptyline(self) -> bool:
        """ method is called when the user
         enters an empty line,
          and it does nothing."""
        pass

    def do_quit(self, arg):
        """methods handle the commands to exit the program."""
        return True

    def do_EOF(self, arg):
        """methods handle the commands to exit the program."""
        print("")
        return True

    def default(self, line):
        """
         the entered command doesn't match any existing method.
         It parses the command
         using regular expressions and
         invokes the corresponding method dynamically.
        """
        args = line.split('.')
        if len(args) < 2 or all([True if element == ""
                                 else False for element in args]):
            print(f"*** Unknown syntax: {line}")
            return False

        string = "self.do_"
        if args[1] == 'all()':
            string += f"all('{args[0]}')"
            eval(string)
        elif 'show(' in args[1]:
            arguments = get_content(args[1]).split(',')
            string += "show('{} {}')".format(args[0],
                                             arguments[0].replace("'", '"'))
            eval(string)
        elif 'count(' in args[1]:
            string += "count('{}')".format(args[0])
            eval(string)
        elif 'destroy(' in args[1]:
            arguments = get_content(args[1]).split(',')
            string += "destroy('{} {}')".format(args[0],
                                                arguments[0].replace("'", '"'))
            eval(string)
        elif 'update(' in args[1]:
            if "{" in get_content(args[1]) and "}" in get_content(args[1]):
                coincidence = re.search(
                    r"\{.*?}", line).group().replace("'", '"')
                dictionary = json.loads(coincidence)
                id = re.search(r'\".*?\"', line).group()
                [self.do_update('{} {}  {}  {}'.
                                format(args[0], id, key, value))
                 for key, value in dictionary.items()]

            else:
                arguments = get_content(args[1]).split(',')
                string += """update('{} {} {} {}')""".format(
                    args[0], arguments[0].replace("'", '"'),
                    arguments[1].replace("'", '"'),
                    arguments[2].replace("'", '"'))
                eval(string)

    def do_count(self, args):
        """
        method retrieves the number of instances of a specific class.
        """
        args = shlex.split(args)
        counter = 0
        for obj in FileStorage.all(self).values():
            if args[0] == obj.__class__.__name__:
                counter += 1
        print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
