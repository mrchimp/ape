
import ape.lib.basecommand
import os
import argparse

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = 'cd'
    prog_description = 'Change working directory.'

    def add_arguments(self):
        self.parser.add_argument('target',
            default = '.',
            help = "The path to move to.",
            nargs=1)

    def call(self):
        """Changes the current working directory.\nType 'cd <directory name>'."""

        target = ' '.join(self.args.target)

        if os.path.exists(target) == 1:
            os.chdir(target)
        else:
            print("Error: Directory doesn't exist")


if __name__ == "__main__":
    Command().run('')
