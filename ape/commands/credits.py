
import ape.lib.basecommand
import os

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = "credits"
    prog_description = "Displays credits and author information."

    def call(self):
        """Displays credits and author information."""

        print("""Ape is made by and (c) 2009-2014 Mr Chimp.
It uses some code by the following people.

Quotes
   From a list compiled by Rudy Velthuis
   http://blogs.teamb.com/rudyvelthuis/2006/07/29/26308
   
Chimpbot
   Based on lukebot.py - python chat bot in 71 lines
   http://pythonism.wordpress.com/2010/04/18/a-simple-chatbot-in-python/

Eliza and Frank
   Both based on 'an Eliza knock-off' by Joe Strout <joe@strout.net> which was 
   subsequently messed about with by Jeff Epler <jepler@inetnebr.com>, 
   Jez Higgins <jez@jezuk.co.uk> and finally Mr Chimp.\n""")


if __name__ == "__main__":
    calc_inst = Command()
    calc_inst.call('')
