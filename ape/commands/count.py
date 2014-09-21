
import os
import ape.lib.basecommand
from random import choice

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = 'count'
    prog_description = 'Count lines of code or files in a dir.'

    def add_arguments(self):
        self.parser.add_argument('unit',
            nargs = "?",
            choices = ['lines', 'files'],
            help = "What to count.",
            default = 'lines')

    def call(self):
        """
        Counts lines or files. 'count' or 'count lines' will count the number of
        lines in files in current dir and subdirs. 'count files' will count the 
        number of files in the current dir and subdirs. Currently only counts 
        lines in PHP, HTML and TXT files.
        """

        unit = self.args.unit

        print("")

        if unit == 'lines':
            print("Counting lines in all files in current directory and sub directories.")
            print("Total lines: " + str(self.linecounter(os.getcwd())))
        elif unit == 'files':
            print("Counting files in current directory and sub directories.")
            print("Total files: " + str(self.filecounter(os.getcwd())))
        else:
            print("Invalid argument.")
            return False

        print("")

    def linecounter(self, mydir):
        """Count lines in text files in the given directory."""

        numlines = 0

        for file in os.listdir(mydir):
            path = mydir + os.sep + file

            if os.path.isdir(path):
                os.chdir(path)
                numlines += self.linecounter(path)
                os.chdir("..")
            else:
                if path.rfind('.php') != -1 or path.rfind('.html') != -1 or path.rfind('.js') != -1 or path.rfind('.txt') != -1:
                    numlines += self.file_len(file)

        return numlines

    def filecounter(self, mydir):
        """Count files in the given directory."""

        filecount = 0

        for file in os.listdir(mydir):
            path = mydir + os.sep + file
            if os.path.isdir(path):
                filecount += self.filecounter(path)
            else:
                filecount += 1

        return filecount


    def file_len(self, fname):
        """Get number of lines in a given file."""

        i = 0

        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        
        return i + 1

if __name__ == "__main__":
    Command().run()
