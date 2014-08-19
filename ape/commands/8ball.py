
import ape.lib.basecommand
from random import choice

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = '8ball'
    prog_description = 'Get answers to your questions.'

    def call(self):
        """Answers your questions."""

        line = '!'
        answers = [
            'Signs point to yes.',
            'Yes.',
            'Reply hazy, try again.',
            'Without a doubt.',
            'My sources say no.',
            'As I see it, yes.',
            'You may rely on it.',
            'Outlook not so good.',
            'It is decidedly so.',
            'Better not tell you now.',
            'Very doubtful.',
            'Yes - definitely.',
            'It is certain.',
            'Cannot predict now.',
            'Most likely.',
            'Ask again later.',
            'My reply is no.',
            'Outlook good.',
            'Don\'t count on it.']

        print('\nLeave input blank to quit\n')

        while True:
            line = input('What is your question? ')
            if line == '':
                break
            print(choice(answers))

if __name__ == "__main__":
    calc_inst = calc()
    calc_inst.call()
