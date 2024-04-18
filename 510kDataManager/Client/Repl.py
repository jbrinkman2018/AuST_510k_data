# read eval print loop 
# prompts console for desired charts

# Jared Brinkman
# 3-26-24

import sys

from Client.Grapher import Grapher
from UploadData.Trimmer import Trimmer

class Repl:
    
    helpString = \
    "What category do you want to see?\n\
    - \"knumber\"\n\
    - \"applicant\"\n\
    - \"dateReceived\"\n\
    - \"decisionDate\"\n\
    - \"SSPIndicator\"\n\
    - \"type\"\n"
    
    helpTrimString = \
    "How do you want to trim your data? <CATEGORY>, <CATEGORYVARIABLE | MINVALUESHOWN> \n\
    Ex.) Applicant, Aust \n\
    Type \"finished\" when done trimming \n\
    Categories\n\
    - \"knumber\"\n\
    - \"applicant\"\n\
    - \"dateReceived\"\n\
    - \"decisionDate\"\n\
    - \"SSPIndicator\"\n\
    - \"type\"\n"
    
    
    def __init__(self) -> None:
        pass
        
    def eval(self, dataEntries):
        print('Welcome to the 510K Data Manager. Let\'s evaluate some Data. Type help to see your options')
        print(self.helpString)
        input =  sys.stdin.readline().strip()
        graphing_input = input
        
        while not input == 'finished':
            
            print(self.helpTrimString)
            input = sys.stdin.readline().strip()
            print(Trimmer(dataEntries).eval(input))
        
        print(self.switch_case(graphing_input, dataEntries))   
        
    def switch_case(self, argument, dataEntries):
            
        if argument == "applicant":
            grapher = Grapher(dataEntries)
            grapher.barhGraph(dataEntries.applicants, "Applicants", "Number of Applications", "Applicant")
            return ""
        
        elif argument == "type":
            grapher = Grapher(dataEntries)
            grapher.barhGraph(dataEntries.types, "Type", "Number of Applications", "Type of Application")
            return ""
        
        # elif argument == "SSPIndicator":
        #     grapher = Grapher(dataEntries)
        #     grapher.barGraph(dataEntries.SSPIndicators, "SSPIndicator", "Number of Applications", "SSP Indicator")
        #     return ""
        
        # elif argument == "decisionDate":
        #     grapher = Grapher(dataEntries)
        #     grapher.barGraph(dataEntries.decisionDates, "Decision Dates", "Number of Applications", "Decision Dates")
        #     return ""
        
        # elif argument == "kNumber":
        #     grapher = Grapher(dataEntries)
        #     grapher.barGraph(dataEntries.kNumbers, "kNumbers", "Number of Applications", "k Numbers")
        #     return ""
        
        # elif argument == "dateReceived":
        #     grapher = Grapher(dataEntries)
        #     grapher.barGraph(dataEntries.dateReceiveds, "Dates Received", "Number of Applications", "Dates Received")
        #     return ""
        
        elif argument == "help":
            return self.helpString
        
        elif argument == "quit":
            return "You quit"
        
        else:
            return ""