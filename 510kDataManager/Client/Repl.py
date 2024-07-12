# high level read eval print loop 
# prompts console for desired charts

# Jared Brinkman
# 3-26-24

import sys

from Client.Grapher import Grapher
from UploadData.Trimmer import Trimmer
from Pluralizer import Pluralizer
from Client.EscapeSequences import EscapeSequences as es

class Repl:
    queryInput = \
    "What would you like to Trim?\n"
    
    categoriesString = \
    "Categories\n\
    - \"knumber\"\n\
    - \"applicant\"\n\
    - \"contact\"\n\
    - \"street1\"\n\
    - \"street2\"\n\
    - \"city\"\n\
    - \"state\"\n\
    - \"countryCode\"\n\
    - \"zip\"\n\
    - \"postalCode\"\n\
    - \"dateReceived\"\n\
    - \"decisionDate\"\n\
    - \"decision\"\n\
    - \"reviewAdviseComm\"\n\
    - \"productCode\"\n\
    - \"stateOrSumm\"\n\
    - \"classAdviceSumm\"\n\
    - \"SSPIndicator\"\n\
    - \"type\"\n\
    - \"thirdParty\"\n\
    - \"expeditedReview\"\n\
    - \"deviceName\"\n"
    
    helpGraphString = \
    "What category do you want to look at (Either Graphed or Printed to Console)?\n"\
    + categoriesString
    
    helpTrimDigit = \
    "How do you want to trim your data using Values? <CATEGORY>, <THRESHOLD>, <max/min> \n\
    Ex.) Applicant + 10 \n"
    
    helpTrimString = \
    "How do you want to trim your data using categories? <CATEGORY>, <CATEGORYVARIABLE> \n\
    Ex.) Applicant + Aust \n\
    Type \"finished\" when done trimming \n\
    Type \"help + <CATEGORY>\" to query available objects to trim in a category\n"\
    + categoriesString
    
    def __init__(self) -> None:
        pass
        
    def eval(self, dataEntries):
        isRetrim = "yes"
        while (isRetrim == "yes"):
            esc = es()
            print(esc.SET_BG_COLOR_WHITE + esc.SET_TEXT_BOLD + esc.SET_TEXT_COLOR_BLUE)
            print('Welcome to the 510K Data Manager. Let\'s evaluate some Data.\n')
            input = 'start'
            print(self.helpTrimString)
            while not input == 'finished':
                print(self.queryInput)
                input = sys.stdin.readline().strip()
                dataEntries = (Trimmer(dataEntries).eval(input, "string"))
            
            dataEntries.calcProperties()
            digitTrim = 'start'
            print(self.helpTrimDigit)
            while not digitTrim == 'finished':
                print(self.queryInput)
                digitTrim= sys.stdin.readline().strip()
                if (digitTrim != 'finished'):
                    dataEntries = (Trimmer(dataEntries).eval(digitTrim, "digit"))
                    
            dataEntries.calcProperties()
            print(self.helpGraphString)
            graphing_input =  sys.stdin.readline().strip()
            
            self.switch_case(graphing_input, dataEntries)
            print("Would you like to retrim? <yes>, <no>")
            isRetrim = sys.stdin.readline().strip()
            print(esc.RESET_BG_COLOR)
            print(esc.RESET_TEXT_COLOR)
    
    # graphing unique graphs and variables for desired scope
    def switch_case(self, argument, dataEntries):
        arguments =Pluralizer.toPlural(argument)
        if (hasattr(dataEntries, arguments)):
            if (len(getattr(dataEntries, arguments)) > 30):
                print("Unable to graph. Please continue trimming and try again\n")
                return
            grapher = Grapher(dataEntries)
            if argument == "applicant":
                grapher.barhGraph(dataEntries.applicants, "Applicants", "Number of Applications", "Applicant")
                return
            elif argument == "type":
                grapher.barhGraph(dataEntries.types, "Type", "Number of Applications", "Type of Application")
                return
            elif argument == "SSPIndicator":
                grapher.barGraph(dataEntries.SSPIndicators, "SSPIndicator", "SSP Indicator", "Number of Applications")
                return
            elif argument == "decisionDate":
                grapher.barGraph(dataEntries.decisionDates, "Decision Dates", "Decision Dates", "Number of Applications")
                return
            elif argument == "kNumber":
                grapher.barGraph(dataEntries.kNumbers, "kNumbers", "k Numbers", "Number of Applications")
                return
            elif argument == "dateReceived":
                grapher.barGraph(dataEntries.dateReceiveds, "Dates Received", "Dates Received", "Number of Applications")
                return
            elif argument == "contact":
                grapher.barhGraph(dataEntries.contacts, "Contact", "Number of Applications", "Contact For Application")
                return
            elif argument == "street1":
                grapher.barGraph(dataEntries.street1s, "Street1", "Contact Street 1", "Number of Applications")
                return
            elif argument == "street2":
                grapher.barGraph(dataEntries.street2s, "Street2", "Contact Street 2", "Number of Applications")
                return
            elif argument == "city":
                grapher.barGraph(dataEntries.cities, "Cities", "Contact City", "Number of Applications")
                return
            elif argument == "state":
                grapher.barGraph(dataEntries.states, "States", "Contact State", "Number of Applications")
                return
            elif argument == "countryCode":
                grapher.barhGraph(dataEntries.countryCode, "Country Code", "Number of Applications", "Contact Country Code")
                return
            elif argument == "zip":
                grapher.barGraph(dataEntries.zips, "Zip", "Contact Zip", "Number of Applications")
                return
            elif argument == "postalCode":
                grapher.barGraph(dataEntries.postalCodes, "Postal Code", "Contact Postal Codes", "Number of Applications")
                return
            elif argument == "decision":
                grapher.barGraph(dataEntries.decisions, "Decision", "Application Decision", "Number of Applications")
                return
            elif argument == "reviewAdviseComm":
                grapher.barGraph(dataEntries.revewAdviseComms, "Review Advise Comm.", "Review Advise Comm.", "Number of Applications")
                return
            elif argument == "productCode":
                grapher.barhGraph(dataEntries.productCodes, "Product Code", "Number of Applications", "Product Code")
                return
            elif argument == "stateOrSumm":
                grapher.barGraph(dataEntries.stateOrSumms, "State or Summ", "State Or Summ", "Number of Applications")
                return
            elif argument == "classAdviceSumm":
                grapher.barGraph(dataEntries.classAdviceSumms, "Class Advice Summ", "Class Advice Summ", "Number of Applications")
                return
            elif argument == "thirdParty":
                grapher.barGraph(dataEntries.thirdParties, "Third Party", "Third Party", "Number of Applications")
                return
            elif argument == "expeditedReview":
                grapher.barGraph(dataEntries.expeditedReviews, "Expedited Review", "Expedited Review", "Number of Applications")
                return
            elif argument == "deviceName":
                grapher.barGraph(dataEntries.deviceNames, "Device Name", "Device Name", "Number of Applications")
                return
        else:
            return "Incomplete argument parameter. Expected <CATEGORY>"