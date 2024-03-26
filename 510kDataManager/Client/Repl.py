# read eval print loop 
# prompts console for desired charts

# Jared Brinkman
# 3-26-24

import sys

from Client.Grapher import Grapher

class Repl:
    def __init__(self) -> None:
        pass
        
    def eval(self, dataEntries):
        print('Welcome to the 510K Data Manager. Let\'s evaluate some Data. Type help to see your options')
        
        input =  sys.stdin.readline().strip()
        print(self.switch_case(input, dataEntries))
        
        while not input == 'quit':
            input = sys.stdin.readline().strip()
            print(self.switch_case(input, dataEntries))
            
    def switch_case(self, argument, dataEntries):
        
        if argument == "at":
            grapher = Grapher(dataEntries)
            grapher.barGraph(dataEntries.APPLICANTS, dataEntries.APPLICANTSVALUES)
            return "having fun"
        
        elif argument == "help":
            return "These are your options \
                - \"a\" : applicants"
                
        elif argument == "quit":
            return "You quit"
        
        else:
            return ""