#!/usr/bin/python3
"""
    Program that contains the entry point of the command interpreter.
"""

from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City
from models.user import User
from models import storage
import shlex
import cmd
import ast
import re


class HBNBCommand(cmd.Cmd):
    """
        class for the command interpreter.
    """

    __classes = ["BaseModel", "User", "State", "City",
                 "Place", "Amenity", "Review"]

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Exits the program. """
        return True

    def emptyline(self):
        """ Skip execution when an empty line is received. """
        pass

    def do_EOF(self, arg):
        """ Exits the program. """
        return True

    def do_create(self, arg):
        """
        - Creates a new instance of ``BaseModel``,
          saves it (to the JSON file) and prints the ``id``.
        """
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")

        elif arg[0] in self.__classes:
            obj = eval(arg[0])()
            obj.save()
            print(obj.id)

        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        - Prints the string representation of an instance
          based on the class name and ``id``
        """
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
            return

        if arg[0] in self.__classes:

            if len(arg) < 2:
                print("** instance id missing **")
                return

            instance = arg[0] + "." + arg[1]
            objects = storage.all()

            try:
                print(objects[instance])

            except KeyError:
                print("** no instance found **")

        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        - Deletes an instance based on the class name and ``id``
          (save the change into the JSON file).
        """
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
            return

        if arg[0] in self.__classes:

            if len(arg) < 2:
                print("** instance id missing **")
                return

            instance = arg[0] + "." + arg[1]
            storage.reload()
            objects = storage.all()

            try:
                del objects[instance]
                storage.save()

            except KeyError:
                print("** no instance found **")

        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name.
        """
        arg = arg.split()

        if len(arg) == 0:
            instances = []
            for key, value in storage.all().items():
                instances.append(value.__str__())
            print(instances)

        elif arg[0] in self.__classes:
            instances = []
            for key, value in storage.all().items():
                if value.__class__.__name__ == arg[0]:
                    instances.append(value.__str__())
            print(instances)

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        - Updates an instance based on the class ``name`` and ``id``
          by adding or updating attribute (save the change into the JSON file).
        """
        arg = shlex.split(arg)

        if len(arg) == 0:
            print("** class name missing **")
            return

        if arg[0] in self.__classes:

            if len(arg) < 2:
                print("** instance id missing **")
                return

            instance = arg[0] + "." + arg[1]
            storage.reload()
            objects = storage.all()

            try:
                if objects[instance]:
                    pass
            except KeyError:
                print("** no instance found **")
                return

            if len(arg) < 3:
                print("** attribute name missing **")
                return

            elif len(arg) < 4:
                print("** value missing **")
                return

            setattr(objects[instance], arg[2], arg[3])
            storage.save()

        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """ Retrieve the number of instances of a class """
        counter = 0

        for key, value in storage.all().items():
            if value.__class__.__name__ == arg:
                counter += 1

        print(counter)

    def default(self, arg):
        """
        - Receive undefined values as methods
          to perform a corresponding execution.
        """
        arg = arg.split(".")

        if arg[0] in self.__classes:

            if arg[1] == "all()":
                self.do_all(arg[0])

            elif arg[1] == "count()":
                self.do_count(arg[0])

            elif re.search("^show(.*$)", arg[1]):
                _id = str(arg[1]).split("(")
                _id = _id[1].replace('"', "").replace(")", "")
                self.do_show(arg[0] + " " + _id)

            elif re.search("^destroy(.*$)", arg[1]):
                _id = str(arg[1]).split("(")
                _id = _id[1].replace('"', "").replace(")", "")
                self.do_destroy(arg[0] + " " + _id)

            elif re.search("^update(.*$)", arg[1]):

                # With a dictionary.
                args = arg[1].split("(")
                args = args[1].split(", ", 1)
                _id = args[0].replace('"', "")
                _dict = ast.literal_eval(args[1].replace(")", ""))

                if type(_dict) == dict:
                    for key, value in _dict.items():
                        _update = arg[0] + " " + _id + " "
                        self.do_update(_update + key + " " + str(value))
                    return

                # With arguments.
                args = re.split(", |\(", arg[1])
                _id = args[1].replace('"', "")
                _name = args[2].replace('"', "")
                _value = args[3].replace('"', "").replace(")", "")
                _update = arg[0] + " " + _id + " " + _name + " " + _value
                self.do_update(_update)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
