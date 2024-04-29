# read eval print loop 
# prompts console for desired charts

# Jared Brinkman
# 3-26-24

import sys

from Client.Grapher import Grapher
from UploadData.Trimmer import Trimmer

class Repl:
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
    "How do you want to trim your data using Values? <CATEGORY>, <THRESHOLD> \n\
    Ex.) Applicant, 10 \n"
    
    helpTrimString = \
    "How do you want to trim your data using categories? <CATEGORY>, <CATEGORYVARIABLE> \n\
    Ex.) Applicant, Aust \n\
    Type \"finished\" when done trimming \n"\
    + categoriesString
    
    def __init__(self) -> None:
        pass
        
    def eval(self, dataEntries):
        isRetrim = "yes"
        while (isRetrim == "yes"):
            print('Welcome to the 510K Data Manager. Let\'s evaluate some Data.')
            print(self.helpTrimString)
            input = 'start'
            while not input == 'finished':
                print(self.helpTrimString)
                input = sys.stdin.readline().strip()
                dataEntries = (Trimmer(dataEntries).eval(input, "string"))
            dataEntries.calcProperties()
            digitTrim = 'start'
            while not digitTrim == 'finished':
                print(self.helpTrimDigit)
                digitTrim= sys.stdin.readline().strip()
                if (digitTrim != 'finished'):
                    dataEntries = (Trimmer(dataEntries).eval(digitTrim, "digit"))

            print(self.helpGraphString)
            graphing_input =  sys.stdin.readline().strip()
            
            self.switch_case(graphing_input, dataEntries)
            print("Would you like to retrim? <yes>, <no>")
            isRetrim = sys.stdin.readline().strip()
        
    def switch_case(self, argument, dataEntries):
        grapher = Grapher(dataEntries)
        if argument == "applicant":
            grapher.barhGraph(dataEntries.applicants, "Applicants", "Number of Applications", "Applicant")
            return
        elif argument == "type":
            grapher.barhGraph(dataEntries.types, "Type", "Number of Applications", "Type of Application")
            return
        elif argument == "SSPIndicator":
            grapher.barGraph(dataEntries.SSPIndicators, "SSPIndicator", "Number of Applications", "SSP Indicator")
            return
        elif argument == "decisionDate":
            grapher.barGraph(dataEntries.decisionDates, "Decision Dates", "Number of Applications", "Decision Dates")
            return
        elif argument == "kNumber":
            grapher.barGraph(dataEntries.kNumbers, "kNumbers", "Number of Applications", "k Numbers")
            return
        elif argument == "dateReceived":
            grapher.barGraph(dataEntries.dateReceiveds, "Dates Received", "Number of Applications", "Dates Received")
            return
        elif argument == "contact":
            grapher.barhGraph(dataEntries.contacts, "Contact", "Number of Applications", "Contact For Application")
            return
        elif argument == "street1":
            grapher.barGraph(dataEntries.street1s, "Street1", "Number of Applications", "Contact Street 1")
            return
        elif argument == "street2":
            grapher.barGraph(dataEntries.street2s, "Street2", "Number of Applications", "Contact Street 2")
            return
        elif argument == "city":
            grapher.barGraph(dataEntries.cities, "Cities", "Number of Applications", "Contact City")
            return
        elif argument == "state":
            grapher.barGraph(dataEntries.states, "States", "Number of Applications", "Contact State")
            return
        elif argument == "countryCode":
            grapher.barhGraph(dataEntries.countryCode, "Country Code", "Number of Applications", "Contact Country Code")
            return
        elif argument == "zip":
            grapher.barGraph(dataEntries.zips, "Zip", "Number of Applications", "Contact Zip")
            return
        elif argument == "postalCode":
            grapher.barGraph(dataEntries.postalCodes, "Postal Code", "Number of Applications", "Contact Postal Codes")
            return
        elif argument == "decision":
            grapher.barGraph(dataEntries.decisions, "Decision", "Number of Applications", "Application Decision")
            return
        elif argument == "reviewAdviseComm":
            grapher.barGraph(dataEntries.revewAdviseComms, "Review Advise Comm.", "Number of Applications", "Review Advise Comm.")
            return
        elif argument == "productCode":
            grapher.barhGraph(dataEntries.productCodes, "Product Code", "Number of Applications", "Product Code")
            return
        elif argument == "stateOrSumm":
            grapher.barGraph(dataEntries.stateOrSumms, "State or Summ", "Number of Applications", "State Or Summ")
            return
        elif argument == "classAdviceSumm":
            grapher.barGraph(dataEntries.classAdviceSumms, "Class Advice Summ", "Number of Applications", "Class Advice Summ")
            return
        elif argument == "thirdParty":
            grapher.barGraph(dataEntries.thirdParties, "Third Party", "Number of Applications", "Third Party")
            return
        elif argument == "expeditedReview":
            grapher.barGraph(dataEntries.expeditedReviews, "Expedited Review", "Number of Applications", "Expedited Review")
            return
        elif argument == "deviceName":
            grapher.barGraph(dataEntries.deviceNames, "Device Name", "Number of Applications", "Device Name")
            return
        else:
            return "Incomplete argument parameter. Expected <CATEGORY>"