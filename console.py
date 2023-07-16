#!/usr/bin/python3
"""
the entry point of the command interpreter
"""
import cmd
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
        comarg = line.split()
        return comarg

    def do_create(self, line):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id"""
        argms = self.parseline(line)
        if len(argms) == 1:
            print("** class name missing **")
        elif argms[1] not in HBNBCommand.__classe:
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
        elif ("{}.{}".format(argms[1], argms[2]) not in storage.all().keys()):
            print("** no instance found **")
        else:
            print(__objects["{}.{}".format(argms[0], argms[1])])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        argms = self.parseline(line)
        if len(argms) == 0:
            print("** class name missing **")
        elif argms[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        elif len(argms) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(argms[1], argms[2]) not in storage.all().keys()):
            print("** no instance found **")
        else:
            del __objects["{}.{}".format(argms[0], argms[1])]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        argms = self.parseline(line)
        if (len(argms) > 0 and argms[0] not in HBNBCommand.__classe):
            print("** class doesn't exist **")
        else:
            inst = []
            for obj in storage.all().values():
                if len(argms) == 0:
                    inst.append(obj.__str__())
                elif (len(argms) > 0 and argms[0] == obj.__class__.__name__):
                    inst.append(obj.__str__())
            print(inst)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        save the change into the JSON file
        Usage: update <class name> <id> <attribute name> <attribute value>"""
        



if __name__ == '__main__':
    HBNBCommand().cmdloop()
