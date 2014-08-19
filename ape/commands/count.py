from random import choice

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = 'count'
    prog_description = 'Count lines of code or files in a dir.'

    def call(self, line):
        """
        Counts lines or files. 'count' or 'count lines' will count the number of
        lines in files in current dir and subdirs. 'count files' will count the 
        number of files in the current dir and subdirs. Currently only counts 
        lines in PHP, HTML and TXT files.
        """
        print("")
        if param == "" or param == "lines":
            print("Counting lines in all files in current directory and sub directories.")
            print("Total lines: " + str(functions.linecounter(os.getcwd())))
        elif param == "files":
            print("Counting files in current directory and sub directories.")
            print("Total files: " + str(functions.filecounter(os.getcwd())))
        print("")

if __name__ == "__main__":
    calc_inst = calc()
    calc_inst.call()
