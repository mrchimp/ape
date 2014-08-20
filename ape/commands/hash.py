
import ape.lib.basecommand
import os
import argparse
import hashlib

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = 'hash'
    prog_description = 'Hash a string.'

    def add_arguments(self):
        self.parser.add_argument('source',
            default = '.',
            help = "String to hash or name of file to hash.",
            nargs=1)

    def call(self):
        """Hashes a string or a file with a chosen algorithm."""

        # strorfile = input("\nWhat do you want to hash?\n\n1. String\n2. File ")

        # List and choose algorithm
        print("\nAvailable algorithms:")

        algos = hashlib.algorithms_available
        i = 0
        source = self.args.source[0]
        chunksize = 128

        for algo in algos:
            print(str(i) + ". " + algo)
            i = i + 1

        print("q. Cancel")

        algorithm = input("\nChoose an algorithm:")

        if algorithm == "q":
            print("Better luck next time.")
            return False

        algorithm = int(algorithm)
        m = hashlib.new(list(algos)[algorithm])

        if os.path.isfile(source):
            print("Hashing file '" + source + "'")

            # filename  = input("\nPlease enter the name of the file to hash.")
            f = open(source, "rb")

            while True:
                data = f.read(chunksize)
                if not data:
                    break
                m.update(data)

            f.close()
        else:
            print("Hashing string '" + source + "'")

            source = source.encode('utf-8')
            m.update(source)

        result = m.hexdigest()

        print("\nResult: " + result + "\n")


if __name__ == "__main__":
    calc_inst = Command()
    calc_inst.call('')
