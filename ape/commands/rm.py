
import os
import shutil
import argparse
import ape.lib.basecommand
from ape.lib.helpers import Helpers

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = 'rm'
    prog_description = 'Delete a file or directory.'

    def add_arguments(self):
        self.parser.add_argument('target',
            default = '.',
            help = "The path to delete. Can be a single file or directory or a comma-separated list of numbers.",
            nargs="+")

    def call(self):
        """Deletes a file or folder. You can specify the files to delete by name or by a list of number(s) given by the DIR command.\nrm example.txt\nrm 6, 8, 12-14"""

        params = self.args.target

        # print(str(params))
        # return

        if params:
            if len(params) > 1: # We have a list of file/dir numbers
                del_list = Helpers.makelist(self.param_str)
                dir_list = os.listdir(os.getcwd())
                errors = 0 

                for x in del_list:
                    try:
                        if os.path.exists(dir_list[x]):
                            os.remove(dir_list[x])
                    except (IndexError):
                        errors += 1

                if errors == len(del_list):
                    print("\nNothing was deleted. Ultimate fail.")
                elif errors > 0:
                    print("\n" + str(errors) + ' files could not be deleted. Check your numbers and try again.\n')
                else:
                    print('\nFiles deleted successfully!\n')
            else: # Only one item - remove it directly
                self.rm_item(params[0])
                        
        else:
            print("PEBKAC Error: correct usage: 'del [filename]'\n")

    def rm_item(self, item):
        if os.path.isdir(item):
            if input("\nReally delete directory '" + item + "' and it's contents? [y/n]: ") == "y":
                shutil.rmtree(item)
                print("Done!")
            else:
                print("Yeah, probably for the best. You'll only realise you need it later on.\n")

        elif os.path.isfile(item):
            sure = input("\nReally delete file '" + item + "'? [y/n]: ")

            if sure == "y":
                os.remove(item)
                print("Done!")
            else:
                print("Fair enough. It's not like you need the disk space.\n")


if __name__ == "__main__":
    calc_inst = Command()
    calc_inst.call('')
