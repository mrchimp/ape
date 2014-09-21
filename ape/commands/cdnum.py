
import ape.lib.basecommand
import os

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = "cdnum"
    prog_description = "Change working directory by number. For use with the DIR command."

    def add_arguments(self):
        self.parser.add_argument("target",
            default = -1,
            help = "The number of the target to move to. Get this from DIR command.",
            type = int,
            nargs = 1)

    def call(self):
        """Changes the current working directory by number.\nFor use with the DIR command."""
        
        dir_list = os.listdir(os.getcwd())

        target_num = self.args.target[0]

        if os.path.exists(dir_list[int(target_num)]):
            try:
                os.chdir(dir_list[int(target_num)])
            except NotADirectoryError:
                print("That isn't a directory.")
        else:
            print("Error: Out of range")


if __name__ == "__main__":
    Command().run('')
