#!/usr/bin/python3
"""
the entry point of the command interpreter
"""
import cmd
import ast
import sys
from models.user import User
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    use the module cmd to implement command interpreter
    """
    prompt = '(hbnb) '
    """we need to create known classe"""
    __classe = {"BaseModel", "User", "State", "City",
                "Place", "Amenity", "Review"}

    def do_quit(self, line):
        """Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """EOF to exit the program """
        return True

    # Help is provided by default by cmd
    def emptyline(self):
        """Shouldn’t execute anything """
        pass

    def parseln(self, line):
        """Splits the line into arguments"""
        argms = line.split()
        return argms

    def do_create(self, line):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id"""
        argms = self.parseln(line)
        if len(argms) == 0:
            print("** class name missing **")
        elif argms[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        else:
            print(eval(argms[0])().id)
            storage.save

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        argms = self.parseln(line)
        if len(argms) == 0:
            print("** class name missing **")
        elif argms[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        elif len(argms) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(argms[0], argms[1]) not in storage.all().keys()):
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(argms[0], argms[1])])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        argms = self.parseln(line)
        if len(argms) == 0:
            print("** class name missing **")
        elif argms[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        elif len(argms) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(argms[0], argms[1]) not in storage.all().keys()):
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(argms[0], argms[1])]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        argms = self.parseln(line)
        if (len(argms) > 0 and argms[0] not in HBNBCommand.__classe):
            print("** class doesn't exist **")
        else:
            inst = []
            for obj in storage.all().values():
                if len(argms) == 0:
                    inst.append(obj.__str__())
                elif (len(argms) > 0 and argms[0] == obj.__class__.__name__):
                    inst.append(obj.__str__())
            cinst = [b.strip("\\") for b in inst]
            print(cinst)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        save the change into the JSON file
        Usage: update <class name> <id> <attribute name> <attribute value>
        we can assume:
            the attribute name is valid
            id, created_at and updated_at won’t be passed
            nobody will try to update list of ids or datetime
            arguments are always in the right order
            Each arguments are separated by a space
            A string argument with a space must be between double quote
        """
        argms = self.parseln(line)
        if len(argms) == 0:
            print("** class name missing **")
        elif argms[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        elif len(argms) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(argms[0], argms[1]) not in storage.all().keys()):
            print("** no instance found **")
        elif len(argms) == 2:
            print("** attribute name missing **")
        elif len(argms) == 3:
            print("** value missing **")
        elif len(argms) >= 4:
            element = storage.all()["{}.{}".format(argms[0], argms[1])]
            setattr(element, argms[2], argms[3])
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
