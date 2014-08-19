# chimpbot.py
#
# Chimp Bot by Jake Gully
# Based on lukebot.py - python chat bot in 71 lines
#   - http://pythonism.wordpress.com/2010/04/18/a-simple-chatbot-in-python/

import os

class Chimpbot:

    import pickle,random

    def __init__(self):
        self.successor_list = ''
        self.current_dict = os.path.dirname(os.path.realpath(__file__)) + '/../../data/default_dict.dat'
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
        b=open(input_file, 'r')
        text=[]
        print(b)
        x = 0
        for line in b:                                                  # For each line of the file
            print("x="+str(x))
            y = 0
            for word in line.split():                                   # split each word into text[]
                print("y="+str(y))
                text.append (word)                                      #
                y = y + 1
            #b.close()                                                  # Close file
            line_list=list(set(text))                                   # split text by line into a list
            #follow={}                                                  #
            for l in range(len(line_list)):                             # for each line in list
                working=[]                                              # 
                check=line_list[l]                                      # 
                for w in range(len(text)-1):                            # Check every letter except the last in each word
                    if check==text[w] and text[w][-1] not in '(),.?!':  #   for punctuation
                        working.append(str(text[w+1]))                  #   append if there's no punctuation
                self.successor_list[check]=working
            x = x + 1
        print(follow)
        b.close()

    def load(self, file_name):
        "Loads a dict file."
        try:
            a=open(file_name,'rb')
            self.successor_list=self.pickle.load(a)
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
        a=open(out_file,'wb')
        pickle.dump(follow,a,2) 
        a.close()

    def say(self, input_str):
        "Pass a string to the bot and return its reply"
        if len(input_str) > 0:
            s=self.random.choice(input_str.split()) # Choose a random word from the input.
        else:
            s = 'the'
        response=''                             # 
        while True:                             # LOOP
            neword=self.nextword(s)             #   pick a random word from the input
            response+=' '+neword                #   concatenate the word
            s=neword                            #   loop around and get the next word
            if neword[-1] in '?,!.':            # IF we get a full stop then end 
                break                           #
        return response                         # Say something

if __name__ == "__main__":
    bot = chimpBot()
    bot.talk()
