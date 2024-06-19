from UploadData.FiveTenEntry import FiveTenEntry
from UploadData.FiveTenEntries import FiveTenEntries
from Pluralizer import Pluralizer
class Trimmer():
    invalidInputString = "Expected: <CATEGORY> + (<CATEGORYVARIABLE> | <THRESHOLDVALUE>) + <max/min> (for digit trim)"
    
    def __init__(self, data):
        self.data = data
        self.removeLater = []
        self.resultEntries = FiveTenEntries()
    
    # function that evaluates the input string and allocates it depending on the parameters
    def eval(self, trimString, digitOrString):
        if (trimString == "finished"):
            return self.data
        trimParams = trimString.split(' + ')
        if (len(trimParams) < 2):
            print(self.invalidInputString)
        elif(trimParams[0] == "help"):
            print(self.data.print(trimParams[1]))
        elif ((digitOrString == "digit") & (len(trimParams) < 3)):
            print(self.invalidInputString)
        elif Pluralizer.toPlural(trimParams[0]) in dir(self.data):
            if (trimParams[1].isdigit()):
                if (digitOrString == "digit"):
                    self.data.trimDigit(trimParams[0], trimParams[1], trimParams[2])
                else:
                    print(self.invalidInputString)
            else:
                if (digitOrString == "string"):
                    for entry in self.data.entryList:
                        if trimParams[1].lower() == getattr(entry, trimParams[0].lower()):
                            self.resultEntries.add(entry)
                    if (len(self.resultEntries.entryList)<1):
                        print(self.invalidInputString)
                else:
                    print(self.invalidInputString)
        else:
             print(self.invalidInputString)
             
        if (len(self.resultEntries.entryList)):
            return self.resultEntries
        else:
            return self.data