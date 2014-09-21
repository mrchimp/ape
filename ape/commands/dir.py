
import ape.lib.basecommand
import os

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = 'dir'
    prog_description = 'List contents of current directory.'

    def call(self):
        """Lists the contents of the current directory."""
        print("")
        self.dir_list = os.listdir(os.getcwd())
        for x in range(len(self.dir_list)):
            print(str(x) + ": " + self.dir_list[x])
        print("" )


if __name__ == "__main__":
    Command().run('')


