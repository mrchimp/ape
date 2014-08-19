
import ape.lib.basecommand
from decimal import *

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = 'calc'
    prog_description = 'Do basic maths.'

    def __init__(self):
        self.func_dict = {
            '+' : self.add,
            '-' : self.subtract,
            '*' : self.multiply,
            '/' : self.divide,
        }
    
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("Divide by 0 error.")
        else:
            return a / b

    def calc(self, oper, a, b):
        try:
            a = Decimal(a)
            b = Decimal(b)
        except InvalidOperation:
            return False
        
        if oper in self.func_dict:
            return self.func_dict[oper](a, b)
        else:
            print("I don't know how to do that.")

    def call(self):
        while True:
            try:
                a = input("Enter a value. Q to quit.")
                if a == 'q':
                    break;
            except ValueError:
                print("There was a problem 1")
                break;
                
            try:
                x = input("Enter an operator.")
            except ValueError:
                print("There was a problem 2")
                break;
                
            try:
                b = input("Enter a second value.")
            except ValueError:
                print("There was a problem 3")
                
            print(self.calc(x, a, b))

    
if __name__ == "__main__":
    calc_inst = Command()
    calc_inst.run('')
