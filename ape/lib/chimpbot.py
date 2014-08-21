# chimpbot.py
#
# Chimp Bot by Jake Gully
# Based on lukebot.py - python chat bot in 71 lines
#   - http://pythonism.wordpress.com/2010/04/18/a-simple-chatbot-in-python/
#
# Todo:
#   Use BeautifulSoup to allow importing from web.
#   Allow line-break spanning word pairs

import os
import pickle
import random
from ape.lib.helpers import Helpers

class Chimpbot:

    follow = {}    # Word/following-word pairs
    dict_file = '' # Dictionary file path

    def __init__(self, default_dict):
        self.successor_list = ''
        self.current_dict = default_dict

        try:
            self.load(self.current_dict)
        except IOError:
            print("Failed to load dictionary.")

    def talk(self):
        "Enters a conversation with Chimpbot"

        print("[o_o] :hello")

        in_str = ''
        
        while in_str != 'quit':
            in_str = input('You   :')

            if in_str == '_add':
                self.add_source(input('Name of file to process:'))
            elif in_str == '_show':
                self.show()
            else:
                print('[o_o] :' + self.say(in_str))

    def show(self):
        "Shows the current dictionary"

        print("Number of entries: "+str(len(self.successor_list)))

        carryon = input("Type 'y' to display all entries: ")

        if (carryon == 'y'):
            print(self.successor_list)

    def new(self):
        "Clears the current dict."

        self.current_dict = input('Path to new dictionary: ')
        self.successor_list = ''
        
    def nextword(self, a):
        "Gets an appropriate word to follow a given word."

        print(self.successor_list)

        if a in self.successor_list:
            return random.choice(self.successor_list[a])
        else:
            return 'the'

    def add_source(self, input_file):
        "add contents of input_file to current successor_list"

        total_lines = 0
        with open(input_file, 'r', encoding='utf-8') as f:
            for total_lines, l in enumerate(f):
                pass
        total_lines = total_lines + 1


        source_file = open(input_file, 'r', encoding='utf-8')
        line_count = 1
        
        print("Importing " + input_file)

        for line in source_file:
            print(Helpers.make_progress_bar(line_count, total_lines))

            line_words = line.split()

            for word_num in range(0, len(line_words) - 1):
                following_words = []
                this_word = line_words[word_num]
                
                if line_words[word_num][-1] in '(),.?!':
                    following_words.append(str(line_words[word_num + 1]))
                
                if len(following_words) > 0:
                    try:
                        self.follow[this_word].extend(following_words)
                    except KeyError:
                        self.follow[this_word] = following_words

            line_count = line_count + 1

        print('Import complete!')

        source_file.close()

    def load(self, file_name):
        "Load a pickled dictionary file."

        a = open(file_name,'rb')
        self.successor_list = pickle.load(a)
        a.close()

    def save(self):
        "Save the current successor list to the current_dict file"
    
        self.current_dict = os.path.realpath(self.current_dict)

        overwriting = False

        if os.path.isfile(self.current_dict):
            if 'y' != input("Overwrite current dictionary ("+self.current_dict+"), Y/N?"):
                print('Cancelling.')
                return;
            overwriting = True
        
        if not overwriting:
            print('Creating new file...')
        
        try:
            a = open(self.current_dict, 'wb')
            pickle.dump(self.follow, a, 2) 
            a.close()
        except FileNotFoundError:
            print("Couldn't save to file '" + self.current_dict + "'. Check path and try again.")

    def say(self, input_str):
        "Pass a string to the bot and return its reply"
        
        if len(input_str) > 0:
            #s = self.random.choice(input_str.split()) # Choose a random word from the input.
            s = input_str.rsplit(' ', 1)[0] # Last word of input
        else:
            s = 'there'
        
        max_words = 20
        word_count = 0
        response = ''                 #
        
        while True:                   # LOOP
            new_word = self.nextword(s) #   pick a random word from the input
            response += ' ' + new_word  #   concatenate the word
            s = new_word                #   loop around and get the next word
            
            if new_word[-1] in '?,!.' or word_count > max_words:  # IF we get a full stop then end 
                break                 #

            word_count = word_count + 1

        return response               # Say something


if __name__ == "__main__":
    bot = chimpBot()
    bot.talk()
