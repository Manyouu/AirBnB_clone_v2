#!/usr/bin/python3
"""Defines the HBNB console."""

import cmd
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """Ignore empty spaces."""
        pass

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        EOF signal to exit the program.
        """
        print("")
        return True

    def do_create(self, line):
        """
        Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...

        Create a new class instance with given keys/values
        and print its id.
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")

            kwargs = {
                key: eval(value) if value[0] != '"'
                else value.strip('"').replace("_", " ")
                for key, value in (x.split("=") for x in my_list[1:])
            }

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance.

        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object that has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = f"{my_list[0]}.{my_list[1]}"
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.

        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object that has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = f"{my_list[0]}.{my_list[1]}"
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
        Usage: all or all <class> or <class>.all()

        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        if not line:
            objects = storage.all()
            print([str(obj) for obj in objects.values()])
            return
        try:
            args = line.split(" ")
            if args[0] not in self.__classes:
                raise NameError()

            objects = storage.all(eval(args[0]))
            print([str(obj) for obj in objects.values()])

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance by adding or updating attribute.

        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object that has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
            AttributeError: when there is no attribute given
            ValueError: when there is no value given
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = split(line, " ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = f"{my_list[0]}.{my_list[1]}"
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()
            obj = objects[key]
            try:
                obj.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                obj.__dict__[my_list[2]] = my_list[3]
                obj.save()
        except SyntaxError:

