
import argparse
import sys

class CmdArgParser(argparse.ArgumentParser):
    def error(self, message):
        """error(message: string)
        
        Prints a usage message and raises an error.
        This should not return - should exit or raise exception
        """
        self.print_usage(sys.stderr)
        print(message)
        raise SyntaxError('Syntax Error. Please try again.')

class BaseCommand:
    """Base command for other commands to extend"""

    args = None
    parser = None
    prog_name = 'basecommand'
    prog_description = 'This is a base command. You probably shouldn\'t be seeing this.'
    line = ""
    command = ""
    param_str = ""

    def add_arguments(self):
        return

    def run(self, line):
        self.line = line
        line_parts = self.line.split(' ',1)
        self.command = line_parts[0]

        if len(line_parts) > 1:
            self.param_str = line_parts[1]

            try:
                self.parse_command(line_parts[1])
            except SyntaxError:
                # Error has been outputted by this point
                return
            except SystemExit:
                # Argparse attempts to exit on errors or -h
                # We don't want to do that.
                return
        else:
            self.command = ""

            try:
                self.parse_command('')
            except SyntaxError:
                return


        self.call()


    def parse_command(self, arg_str):
        """Interpret command arguments"""
        
        self.parser = CmdArgParser(prog = self.prog_name,
                            description = self.prog_description)
        self.add_arguments()
        self.args = self.parser.parse_args(arg_str.split())

