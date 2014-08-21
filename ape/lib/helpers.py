
class Helpers:

    def makelist(mystr):
        "Take a comma delimited string of numbers and ranges and return a list"
        
        templist = mystr.split(",") # explode

        for z in range(len(templist)): # remove whitespace
            templist[z] = templist[z].strip()

        finallist = []

        for x in range(len(templist)):
            if templist[x].isdigit():               # if item is number then add to list
                finallist.append(int(templist[x]))
            else:                                   # else add range...
                span = str(templist[x]).split("-")
                for y in range(int(span[0]), (int(span[1]) + 1)):
                    finallist.append(y)
                    
        return finallist

    def make_progress_bar(value, total):
        "Create a progress bar from a value and a total."

        import shutil
        (width, height) = shutil.get_terminal_size((80, 20))
        width = width - 2

        perc = int((value / total) * width)
        return '[' + ('-'*perc) + (' '*(width - perc)) + ']'
