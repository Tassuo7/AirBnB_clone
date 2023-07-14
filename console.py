#!/usr/bin/python3
"""
the entry point of the command interpreter
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    use the module cmd to implement command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ quit to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF to exit the program """
        return True

    # Help is provided by default by cmd
    def emptyline(self):
        """ shouldn’t execute anything """
        pass

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
