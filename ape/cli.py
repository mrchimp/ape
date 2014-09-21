#!/usr/bin/env python

"""cli.py - Command line interface for Ape commands"""

import os
import cmd
import pickle
import importlib
import ape.lib.helpers
from random import choice
from ape.lib.clicolors import Clicolors
from ape.lib.chimpbot import Chimpbot

__author__      = "Jacob Gully"
__copyright__   = "Copyright 2009-2014 Jacob Gully"
__license__     = "MIT"
__version__     = "0.0.1"
__maintainer__  = "Jacob Gully"
__email__       = "chimpytk@gmail.com"

class Cli(cmd.Cmd):
    """Ape CLI"""

    prog_name = 'cli'
    prog_description = 'Ape CLI.'
    prompt = ""
    intro = ""
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
    available_commands = [
        '8ball',
        'brename',
        'calc',
        'cd',
        'cdnum',
        'count',
        'credits',
        'dir',
        'rm'
    ]
    quotes_file_dat = os.path.realpath(os.path.dirname(__file__) + '/../data/quotes.dat')
    quotes_file_txt = os.path.realpath(os.path.dirname(__file__) + '/../input/quotes.txt')
    chimpbot_brain_dir = os.path.realpath(os.path.dirname(__file__) + '/../data/')


    def __init__(self):
        super(Cli, self).__init__()
        self.prompt = self.make_prompt()
        print('Loading brain file: ' + self.chimpbot_brain_dir + '/default_dict.dat')
        self.chimpbot = Chimpbot(self.chimpbot_brain_dir, 'default_dict')
        self.intro = self.make_intro()

    def make_intro(self):
        """Create welcome message"""

        intro = "\nApe CLI [Version "+__version__+"]\n"
        intro += __copyright__+"\n\n"

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
        
        intro += choice(self.quotes_array)

        return intro

    def make_prompt(self):
        """Construct a prompt string."""
        
        prompt = Clicolors.HEADER + os.getcwd() + "\n$ " + Clicolors.ENDC
        return prompt.replace(os.getenv('HOME'), '~')

    def postloop(self):
        """Prints a goodbye message."""
        
        print("\nGoodbye!")

    def postcmd(self, stop, line):
        """Executed after each command."""
        
        self.prompt = self.make_prompt()
        return cmd.Cmd.postcmd(self, stop, line)

    def default(self, line):
        """
        Called if a command is not recognised. 
        Try importing command or display a random response from Chimpbot.
        """

        mmodule = importlib.import_module('ape.commands.' + line.split(' ', 1)[0])
        cclass = getattr(mmodule, 'Command')
        cmd = cclass()
        cmd.run(line)

        # @todo except here catches exceptions in the imported modules.
        # This is a pain for developing.
        # try:        
        #     mmodule = importlib.import_module('ape.commands.' + line.split(' ', 1)[0])
        #     cclass = getattr(mmodule, 'Command')
        #     cmd = cclass()
        #     cmd.run(line)
        # except ImportError:
        #     print("\nError: unknown command.\nChimpbot says: " + self.chimpbot.say(line) + "\n")
        #     return
    
    def do_help(self, line):
        print(self.doc_header);
        print(' '*4 + ', '.join(self.available_commands))
        print('')

    def do_quit(self, line):
        return True;

    def do_loaddir(self, line):
        dir_list = os.listdir(os.getcwd())
        for x in range(len(dir_list)):
            print('file: ' + dir_list[x])
            self.chimpbot.add_source(dir_list[x])
        self.chimpbot.save()

    def do_loadtest(self, line):
        self.chimpbot.add_source('input/2001.txt')
        self.chimpbot.save()

    def do_say(self, line):
        print(self.chimpbot.say(line))

    def do_words(self, line):
        if line:
            print(str(self.chimpbot.pairs[line]))
        else:
            print(str(self.chimpbot.pairs))

    def do_loadurl(self, line):
        self.chimpbot.add_url(line, preview = True, depth = 1)

    def do_newbrain(self, line):
        self.chimpbot.new();

if __name__ == '__main__':
    Cli().cmdloop()
