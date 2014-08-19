import os

class Command():

    def call(self, line):
        """Bulk file/folder rename."""

        dir_list = os.listdir(os.getcwd())
        find = input("Text to find: ")
        replace = input("Text to insert: ")
        for x in dir_list:
            if x.find(find) != -1:
                try:
                    os.rename(x, x.replace(find, replace))
                except WindowsError:
                    print("That didn't work. Is it being used? Are you sure you have permission?")


if __name__ == "__main__":
    calc_inst = calc()
    calc_inst.call()
