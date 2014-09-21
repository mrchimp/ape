
import ape.lib.basecommand
import os
import argparse

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = 'hello'
    prog_description = 'Speak to an AI.'

    def add_arguments(self):
        self.parser.add_argument('bot',
            default = 'chimpbot',
            help = "Name of the bot to talk to. Available bots: chimpbot (default), eliza.",
            nargs="?")

    def call(self):
        """Start a conversation with a bot."""

        bot = self.args.bot
        
        if bot == "chimpbot":
            print("\nType 'quit' to exit.\n")
            
            from ape.lib.chimpbot import Chimpbot
            
            bot = Chimpbot(os.path.dirname(os.path.realpath(__file__)) + '/../../data/default_dict.dat')
            bot.talk()
            # chimpbot.talk()
        elif bot == 'eliza':
            print("\nType '(quit)' to exit.\n")

            import ape.lib.eliza
            
            ape.lib.eliza.start()

        else:
            print('Who?')


if __name__ == "__main__":
    Command().run('')
