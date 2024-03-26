# read eval print loop 
# prompts console for desired charts

# Jared Brinkman
# 3-26-24

import sys

from Client.Grapher import Grapher

class Repl:
    helpString = \
    "These are your options\n\
    - \"knumber\"\n\
    - \"applicants\"\n\
    - \"dateReceived\"\n\
    - \"decisionDate\"\n\
    - \"SSPIndicator\"\n\
    - \"types\"\n"
    
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
            
        if argument == "applicants":
            grapher = Grapher(dataEntries)
            grapher.barGraph(dataEntries.applicants, "Applicants", "Number of Applications", "Applicant")
            return ""
        
        elif argument == "type":
            grapher = Grapher(dataEntries)
            grapher.barGraph(dataEntries.types, "Type", "Number of Applications", "Type of Application")
            return ""
        
        elif argument == "help":
            return self.helpString
        
        elif argument == "quit":
            return "You quit"
        
        else:
            return ""