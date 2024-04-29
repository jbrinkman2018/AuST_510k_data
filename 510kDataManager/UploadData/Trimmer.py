from UploadData.FiveTenEntry import FiveTenEntry
from UploadData.FiveTenEntries import FiveTenEntries
class Trimmer():
    
    def __init__(self, data):
        self.data = data
        self.removeLater = []
        self.resultEntries = FiveTenEntries()
    
    def eval(self, trimString):
        if (trimString == "finished"):
            return self.data
        trimParams = trimString.split(', ')
        if (len(trimParams) < 2):
            print("Expected: <CATEGORY>, <CATEGORYVARIABLE>")
        elif self.toPlural(trimParams[0].lower()) in dir(self.data):
            print("in selfdata")
            if (trimParams[1].isdigit()):
                print("Expected: <CATEGORY>, <CATEGORYVARIABLE>")
                # self.trimDigit(trimParams[0], int(trimParams[1]))
            else:
                for entry in self.data.entryList:
                    if trimParams[1].lower() == getattr(entry, trimParams[0].lower()):
                        self.resultEntries.add(entry)
                if (len(self.resultEntries.entryList)<1):
                    print("Expected: <CATEGORY>, <CATEGORYVARIABLE> (in ~len)")
        else:
             print("Expected: <CATEGORY>, <CATEGORYVARIABLE>")
             
        if (len(self.resultEntries.entryList)):
            return self.resultEntries
        else:
            return self.data
        
    def toPlural(self, word):
        if word.endswith('y'):
            return word[:-1] + 'ies'
        elif word[-1] in ['s', 'x', 'z'] or word[-2:] in ['sh', 'ch']:
            return word + 'es'
        else:
            return word + 's'