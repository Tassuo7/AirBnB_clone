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
        """ quit to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF to exit the program """
        return True

    # Help is provided by default by cmd
    def emptyline(self):
        """ shouldn’t execute anything """
        pass

    def parseline(self, line):
        """splits the line into arguments"""
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

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
