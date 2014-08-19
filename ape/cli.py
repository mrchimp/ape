#!/usr/bin/env python

"""cli.py - Command line interface for Ape commands"""


import os
import cmd
import pickle
import importlib
from random import choice
from ape.lib.chimpbot import Chimpbot

__author__      = "Jacob Gully"
__copyright__   = "Copyright 2009-2014 Jacob Gully"
__license__     = "MIT"
__version__     = "0.0.1"
__maintainer__  = "Jacob Gully"
__email__       = "chimpytk@gmail.com"

class Cli(cmd.Cmd):
    """Ape CLI"""

    prompt = ""
    quotes_file_dat = ""
    quotes_file_txt = ""
    quotes_array = []
    doc_header = """
    +------------------------------------------------------+
    |        Ape - Command line interface for stuff.       |
    |                                                      |
    |       Below is a list of all available commands.     |
    | Type 'help <command>' to learn more about a command. |
    +------------------------------------------------------+
    """
    undoc_header = "You'll have to figure these out on your own:\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    def __init__(self):
        super(Cli, self).__init__()
        self.prompt = self.make_prompt()
        self.quotes_file_dat = os.path.dirname(os.path.realpath(__file__)) + '/../data/quotes.dat'
        self.quotes_file_txt = os.path.dirname(os.path.realpath(__file__)) + '/../input/quotes.txt'


    def make_prompt(self):
        """Construct a prompt string."""
        
        prompt = os.getcwd() + " >"
        return prompt.replace(os.getenv('HOME'), '~')

    def preloop(self):
        """Display welcome text and load Chimpbot."""

        self.chimpbot = Chimpbot()

        print("\nApe CLI [Version "+__version__+"]")
        print(__copyright__+"\n")

        # Quote of the minute
        try:
            quote_dat_file = open(self.quotes_file_dat, 'rb')
            self.quotes_array = pickle.load(quote_dat_file)
        except:
            try:
                print("Getting quotes from text file...")
                quote_file = open(self.quotes_file_txt, 'r')
                x = 0
                self.quotes_array = []
                for line in quote_file:
                    if line == b'.\n' or line == '.\n':
                        x = x + 1
                    else:
                        try: 
                            self.quotes_array[x] += line
                        except IndexError:
                            self.quotes_array.append(line)
                quote_file.close()
                # pickle results
                quote_dat_file = open(self.quotes_file_dat, 'wb')
                pickle.dump(self.quotes_array, quote_dat_file)
                quote_dat_file.close()
            except IOError:
                self.quotes_array = ['Quotes array is empty.']
        
        print(choice(self.quotes_array))

    def postloop(self):
        """Prints a goodbye message."""
        
        print("\nGoodbye!")

    def postcmd(self, stop, line):
        """Executed after each command. Currently used to update the cmd prompt."""
        
        self.prompt = self.make_prompt()
        return cmd.Cmd.postcmd(self, stop, line)

    def my_import(name):
        mod = __import__(name)
        components = name.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod

    def default(self, line):
        """
        Called if a command is not recognised. 
        Try importing command or display a random response from Chimpbot.
        """
    
        # Command = importlib.import_module('ape.commands.' + line.split(' ', 1)[0])
        # Command.call()

        try:        
            mmodule = importlib.import_module('ape.commands.' + line.split(' ', 1)[0])
            cclass = getattr(mmodule, 'Command')
            cmd = cclass()
            cmd.run(line)
        except ImportError:
            print("\nChimpbot says: Error. " + self.chimpbot.say(line) + "\n")
    




if __name__ == '__main__':
    cli_mate().cmdloop()
