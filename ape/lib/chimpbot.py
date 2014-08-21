# chimpbot.py
#
# Chimp Bot by Jake Gully
# Based on lukebot.py - python chat bot in 71 lines
#   - http://pythonism.wordpress.com/2010/04/18/a-simple-chatbot-in-python/
#
# @todo:
# Allow adding by url
# Allow crawling links in URLs


import os
import pickle
import random

class Chimpbot:

    def __init__(self, default_dict):
        self.successor_list = ''
        self.current_dict = default_dict
        self.load(self.current_dict)

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

        self.current_dict = input('Name your new bot: ')
        self.successor_list = ''
        
    def nextword(self, a):
        "Gets an appropriate word to follow a given word."

        if a in self.successor_list:
            return self.random.choice(self.successor_list[a])
        else:
            return 'the'

    def add_source(self, input_file):
        "add contents of input_file to current successor_list"

        print("Attempting to import " + input_file)
        
        source_file = open(input_file, 'r')
        words = []
        
        print(source_file)
        
        line_count = 0
        
        follow = {}

        for line in source_file:                                                  # For each line of the file
            print("line_count=" + str(line_count))
            
            word_count = 0
            
            # Look through words in lin
            # add them to list
            for word in line.split():                                   # split each word into text[]
                # print("word_count=" + str(word_count))
                words.append(word)
                word_count = word_count + 1
            
            # Duplicate list
            line_list = list(set(words))                                 # split text by line into a list

            for l in range(len(line_list)):                             # for each line in list
                clean_words = []                                            # 
                check = line_list[l]                                    # 
                
                for w in range(len(words)-1):                            # Check every letter except the last in each word
                    if check == words[w] and words[w][-1] not in '(),.?!':  #   for punctuation
                        clean_words.append(str(words[w+1]))                  #   append if there's no punctuation

                follow[check] = clean_words

            line_count = line_count + 1

        print(follow)

        source_file.close()

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
        "Loads a dict file."

        try:
            a = open(file_name,'rb')
            self.successor_list = self.pickle.load(a)
            a.close()
        except IOError:
            print("Failed to load dictionary.")

            self.new()  

    def save(self):
        "save the current successor list to the current_dict file"
        
        overwrite = input("Overwrite current dictionary ("+self.current_dict+"), Y/N?")
        
        if overwrite == "n" or overwrite == "N":
            out_file = input("Enter file name:")
        else:
            out_file = self.current_dict
        
        a = open(out_file,'wb')
        pickle.dump(follow,a,2) 
        a.close()

    def say(self, input_str):
        "Pass a string to the bot and return its reply"
        
        if len(input_str) > 0:
            s = self.random.choice(input_str.split()) # Choose a random word from the input.
        else:
            s = 'the'
        
        response = ''                 #
        
        while True:                   # LOOP
            neword = self.nextword(s) #   pick a random word from the input
            response += ' ' + neword  #   concatenate the word
            s = neword                #   loop around and get the next word
            
            if neword[-1] in '?,!.':  # IF we get a full stop then end 
                break                 #

        return response               # Say something
        

if __name__ == "__main__":
    bot = chimpBot()
    bot.talk()
