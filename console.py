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


class HBNBCommand(cmd.Cmd):
    """
        class for the command interpreter.
    """

    __classes = ["BaseModel", "User",
                 "State", "City",
                 "Place", "Amenity",
                 "Review"]

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
