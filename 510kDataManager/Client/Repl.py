# read eval print loop 
# prompts console for desired charts

# Jared Brinkman
# 3-26-24

import sys

from Client.Grapher import Grapher
from UploadData.Trimmer import Trimmer

class Repl:
    printOrGraph = \
    "Would you like to print the data to console <p> or Graph it. <g>"

    helpGraphString = \
    "What category do you want to look at (Either Graphed or Printed to Console)?\n\
    - \"knumber\"\n\
    - \"applicant\"\n\
    - \"dateReceived\"\n\
    - \"decisionDate\"\n\
    - \"SSPIndicator\"\n\
    - \"type\"\n"
    
    helpTrimString = \
    "How do you want to trim your data using categories? <CATEGORY>, <CATEGORYVARIABLE> \n\
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
        isRetrim = "yes"
        isFirst = "yes"
        while (isRetrim == "yes"):
            print('Welcome to the 510K Data Manager. Let\'s evaluate some Data.')
            print(self.helpTrimString)
            input = 'start'
        
            while not input == 'finished':
                print(self.helpTrimString)
                input = sys.stdin.readline().strip()
            
                dataEntries = (Trimmer(dataEntries).eval(input))
            
            dataEntries.calcProperties()
            
            digitTrim = 'start'
            while not digitTrim == 'finished':
                print(self.helpTrimDigit)
                digitTrim= sys.stdin.readline().strip()
                
                if (digitTrim != 'finished'):
                    
                    if (digitTrim.isdigit):
                        dataEntries = dataEntries.trimDigit(digitTrim)
                    else:
                        print("Expected: <CATEGORY>, <DIGIT>")

            print(self.helpGraphString)
            graphing_input =  sys.stdin.readline().strip()
        
            print(self.printOrGraph)
            printOrGraphInput = sys.stdin.readline().strip()
        
            if (printOrGraphInput == "g"):
                self.switch_case(graphing_input, dataEntries)
            else:
                print("printing desired category")
                # print(desired Category)
            print("Would you like to retrim? <yes>, <no>")
            isRetrim = sys.stdin.readline().strip()
        
    def switch_case(self, argument, dataEntries):
            
        if argument == "applicant":
            grapher = Grapher(dataEntries)
            grapher.barhGraph(dataEntries.applicants, "Applicants", "Number of Applications", "Applicant")
            return ""
        
        elif argument == "type":
            grapher = Grapher(dataEntries)
            grapher.barhGraph(dataEntries.types, "Type", "Number of Applications", "Type of Application")
            return ""
        
        elif argument == "SSPIndicator":
            grapher = Grapher(dataEntries)
            grapher.barGraph(dataEntries.SSPIndicators, "SSPIndicator", "Number of Applications", "SSP Indicator")
            return ""
        
        elif argument == "decisionDate":
            grapher = Grapher(dataEntries)
            grapher.barGraph(dataEntries.decisionDates, "Decision Dates", "Number of Applications", "Decision Dates")
            return ""
        
        elif argument == "kNumber":
            grapher = Grapher(dataEntries)
            grapher.barGraph(dataEntries.kNumbers, "kNumbers", "Number of Applications", "k Numbers")
            return ""
        
        elif argument == "dateReceived":
            grapher = Grapher(dataEntries)
            grapher.barGraph(dataEntries.dateReceiveds, "Dates Received", "Number of Applications", "Dates Received")
            return ""
        
        elif argument == "help":
            return self.helpString
        
        elif argument == "quit":
            return "You quit"
        
        else:
            return "Incomplete argument parameter"