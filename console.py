#!/usr/bin/python3
"""
the entry point of the command interpreter
"""
import cmd
import sys
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    use the module cmd to implement command interpreter
    """
    prompt = '(hbnb) '
    """we need to create known classe"""
    __classe = {"BaseModel"}

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

    def parseline(self, line):
        """Splits the line into arguments"""
        arguments = cmd.Cmd.parseline(self, line)
        return arguments

    def do_create(self, line):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id"""
        argms = self.parseline(line)
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
        argms = self.parseline(line)
        if len(argms) == 0:
            print("** class name missing **")
        elif argms[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        elif len(argms) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(argms[0], argms[1]) not in __objects.keys()):
            print("** no instance found **")
        else:
            print(__objects["{}.{}".format(argms[0], argms[1])])



if __name__ == '__main__':
    HBNBCommand().cmdloop()
