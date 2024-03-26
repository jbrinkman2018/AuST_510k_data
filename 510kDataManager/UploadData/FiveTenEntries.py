# Collection of 510K entries 

class FiveTenEntries:
    def __init__(self):
        self.entryList = []
        self.categories = []
        
    def add(self, entry):
        self.entryList.append(entry)
        
    def calcProperties(self):
        # FIX CALC PROPERTIES
        # build out self.categories.append()
        for entry in self.entryList:# Check if the item is already in the dictionary
            for category in entry:
                if category in self.applicants: # If it is, increment the count
                    self.applicants[category] += 1
                else:
                    # If it's not, add it to the dictionary with a count of 1
                    self.applicants[category] = 1
        
        self.TYPES = [entry.TYPE for entry in self.entryList]
        