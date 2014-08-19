import os

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = 'cd'
    prog_description = 'Change working directory.'

    def call(self, line):
        """Changes the current working directory.\nType 'cd <directory name>'."""

        dest = os.getcwd() + '/' + line.split(' ',1)[1]
        if os.path.exists(dest) == 1:
            os.chdir(dest)
        else:
            print("Error: Directory doesn't exist")


if __name__ == "__main__":
    calc_inst = calc()
    calc_inst.call()
