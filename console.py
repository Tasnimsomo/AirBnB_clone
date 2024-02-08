#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Simple command processor."""
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Handle End-Of-File."""
        return True

    def empty_line(self):
        """Called when an empty line is entered."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
