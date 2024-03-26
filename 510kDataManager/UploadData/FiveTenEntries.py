# Collection of 510K entries 

class FiveTenEntries:
    MIN_APPLICANTS_VALUE = 150
    MIN_TYPES_VALUE = 10
    removeApplicantsLater = []
    removeTypesLater = []
    
    def __init__(self):
        self.entryList = []
        self.kNumbers = dict()
        self.applicants = dict()
        self.contacts = dict()
        self.street1s = dict()
        self.street2s = dict()
        self.cities = dict()
        self.states = dict()
        self.countryCodes = dict()
        self.zips = dict()
        self.postalCodes = dict()
        self.dateReceiveds = dict()
        self.decisionDates = dict()
        self.decisions = dict()
        self.reviewAdviseComms = dict()
        self.productCodes = dict()
        self.stateOrSumms = dict()
        self.classAdviceSumms = dict()
        self.SSPIndicators = dict()
        self.types = dict()
        self.thirdParties = dict()
        self.expeditedReviews = dict()
        self.deviceNames = dict()
        
    def add(self, entry):
        self.entryList.append(entry)
        
    def calcProperties(self):
        for entry in self.entryList:# Check if the item is already in the dictionary
            if entry.applicant in self.applicants: 
                # If it is, increment the count
                self.applicants[entry.applicant] += 1
            else:
                # If it's not, add it to the dictionary with a count of 1
                self.applicants[entry.applicant] = 1
                
            if entry.type in self.types: 
                # If it is, increment the count
                self.types[entry.type] += 1
            else:
                # If it's not, add it to the dictionary with a count of 1
                self.types[entry.type] = 1
                
        for applicant in self.applicants:
            if (self.applicants[applicant] < self.MIN_APPLICANTS_VALUE):
                self.removeApplicantsLater.append(applicant)
        
        for type in self.types:
            if (self.types[type] < self.MIN_TYPES_VALUE):
                self.removeTypesLater.append(type)        
        
        for applicantIndex in self.removeApplicantsLater:
            del self.applicants[applicantIndex]
        
        for typeIndex in self.removeTypesLater:
            del self.types[typeIndex]
            
        self.applicants = dict(sorted(self.applicants.items(), key=lambda item: item[1], reverse=False))
        self.types = dict(sorted(self.types.items(), key=lambda item: item[1], reverse=False))
