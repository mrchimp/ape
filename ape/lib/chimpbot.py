# chimpbot.py
#
# Chimp Bot by Jake Gully
# Based on lukebot.py - python chat bot in 71 lines
#   - http://pythonism.wordpress.com/2010/04/18/a-simple-chatbot-in-python/
#
# Todo:
#   Use BeautifulSoup to allow importing from web.
#   Allow crawling links in URLs
#   Allow line-break spanning word pairs

import os
import pickle
import random
import shutil
import itertools
import time
import sys
from ape.lib.helpers import Helpers
from collections import defaultdict

class Chimpbot:

    pairs = {}    # Word/following-word pairs
    dict_file = '' # Dictionary file path
    terminators = '.!?'
    default_response = 'Erm.'
    max_words = 20
    dict_dir = os.path.realpath(os.path.dirname(__file__) + '../data')

    def __init__(self, dict_dir, dict_name):
        self.dict_dir = dict_dir
        self.current_dict = self.dict_dir + '/' + dict_name + '.dat'

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

    def new(self, name):
        "Clears the current dict."

        self.current_dict = input('Name of brain: ')
        self.pairs = {}
        self.save()
        
    def next_word(self, first_word):
        "Gets an appropriate word to follow a given word."

        if first_word[-1] == ',':
            first_word = first_word[:-1]

        try:
            weights = [x[1] for x in self.pairs[first_word]]
            totals = list(itertools.accumulate(weights))

            rand = random.uniform(0, totals[-1])
            for i, total in enumerate(totals):
                if rand <= total:
                    return self.pairs[first_word][i][0]
        except KeyError:
            return False

    def find_pair_num(self, first_word, second_word):
        """
        Find the index of a given next word
        Returns -1 if first_word doesn't exist
        Returns -2 if second_word doesn't exist
        """

        try:
            for word_num in range(0, len(self.pairs[first_word])):
                if (self.pairs[first_word][word_num][0] == second_word):
                    return word_num
            return -2
        except KeyError:
            return -1

    def add_source(self, input_file):
        "add contents of input_file to current successor_list"

        total_lines = 0
        source_file = open(input_file, 'r', encoding='utf-8')

        print("Importing " + input_file)
        print('Getting word list...')

        all_words = []

        for line in source_file:
            total_lines = total_lines + 1
            for word in line.split():
                all_words.append(word)

        print('Found ' + str(total_lines) + ' lines, ' + str(len(all_words)) + ' words.')

        total_lines = total_lines + 1
        word_count = 1

        source_file.seek(0)
        for word_num in range(0, len(all_words) - 1):
            # print(Helpers.make_progress_bar(word_count, len(all_words)))
            self.update_progress(word_count / len(all_words));
            word_count = word_count + 1

            # If this is a terminating word then skip
            if all_words[word_num][-1] in ').,?!':
                continue

            word = all_words[word_num]
            next_word = all_words[word_num + 1]
            word_num = self.find_pair_num(word, next_word)

            if word_num >= 0:
                # Additional use of pair
                self.pairs[word][word_num] = (next_word, int(self.pairs[word][word_num][1]) +  1)
            elif word_num == -1:
                # New first word
                self.pairs[word] = [(next_word, 1)];
            elif word_num == -2:
                # New second word
                self.pairs[word].append((next_word, 1))
            else:
                print('Pretty sure this shouldn\'t happen.')
            
        print('Import complete!')
        print(str(len(all_words)) + ' words.')

        source_file.close()

    def update_progress(self, progress):
        """
        update_progress() : Displays or updates a console progress bar
        Accepts a float between 0 and 1. Any int will be converted to a float.
        A value under 0 represents a 'halt'.
        A value at 1 or bigger represents 100%
        """

        # shutil.get_terminal_size((80, 20)).columns
        barLength = 20 # @todo magic number!
        status = ""
        if isinstance(progress, int):
            progress = float(progress)
        if not isinstance(progress, float):
            progress = 0
            status = "error: progress var must be float\r\n"
        if progress < 0:
            progress = 0
            status = "Halt...\r\n"
        if progress >= 1:
            progress = 1
            status = "Done...\r\n"
        block = int(round(barLength*progress))
        text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
        sys.stdout.write(text)
        sys.stdout.flush()

    def add_url(self, url, preview=False, depth=1):
        "Get contents of a URL and parse the text."

        from bs4 import BeautifulSoup
        from urllib.request import Request, urlopen
        from urllib.request import URLError

        if url[0:7] != 'http://' and url[0:8] != 'https://':
            url = 'http://' + url

        req = Request(url)
        
        the_text = ''

        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print("Failed to reach server.")
                print("Reason: ", e.reason)
            elif hasattr(e, 'code'):
                print("The server couldn't fulfill the request.")
                print("Error code: ", e.code)

            return False
        else:
            html = response.read()
            soup = BeautifulSoup(html)
            
            for el in soup.find_all(["h1", "h2", "h3", "p"]):
                if el.string:
                    the_text = the_text + el.string

        if preview:
            print('The following would be parsed:\n\n')
            print(the_text)
        else:
            # @todo - do actual importing
            print('No importing yet...')

        # @todo - allow following URLs to given depth

    def load(self, file_name):
        "Load a pickled dictionary file."

        a = open(file_name,'rb')
        self.pairs = pickle.load(a)
        a.close()

    def save(self):
        "Save the current successor list to the current_dict file"
    
        self.current_dict = os.path.realpath(self.current_dict)

        overwriting = False

        if os.path.isfile(self.current_dict):
            if 'y' != input("Overwrite current dictionary ("+self.current_dict+"), Y/N?"):
                print('Cancelling.')
                return
            overwriting = True
        
        if not overwriting:
            print('Creating new file...')
        
        try:
            f = open(self.current_dict, 'wb')
            pickle.dump(self.pairs, f, 2)
            f.close()
        except FileNotFoundError:
            print("Couldn't save to file '" + self.current_dict + "'. Check path and try again.")

    def say(self, input_str):
        "Pass a string to the bot and return its reply"
        
        if len(input_str) > 0:
            #input_word = self.random.choice(input_str.split()) # Choose a random word from the input.
            input_word = input_str.rsplit(' ', 1)[-1] # Last word of input
        else:
            input_word = 'there' # @todo: make this not stupid
        
        word_count = 0
        response = input_str.title()
        current_word = input_str

        while True:
            next_word = self.next_word(current_word)

            # Tidy up end of sentence
            if next_word == False:
                break

            response += ' ' + next_word

            if word_count > self.max_words:
                break

            if response[-1] in self.terminators:
                break

            current_word = next_word
            word_count += 1


        while response[-1] in ',. (:':
            response = response[:-1]

        response += '.'

        return response
        

if __name__ == "__main__":
    bot = chimpBot()
    bot.talk()
