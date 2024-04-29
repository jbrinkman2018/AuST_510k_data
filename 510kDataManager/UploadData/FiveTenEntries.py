# Collection of 510K entries 

class FiveTenEntries:
    # MIN_APPLICANTS_VALUE = 150
    DEFAULT_THRESHOLD = 0
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
        
    def allocateVariables(self, entry):
        ## APPLICANT
        if entry.applicant in self.applicants: 
            # If it is, increment the count
            self.applicants[entry.applicant] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.applicants[entry.applicant] = 1
        ## TYPE  
        if entry.type in self.types: 
            # If it is, increment the count
            self.types[entry.type] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.types[entry.type] = 1
        ## KNUMBER  
        if entry.kNumber in self.kNumbers: 
            # If it is, increment the count
            self.kNumbers[entry.kNumber] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.kNumbers[entry.kNumber] = 1
        ##SSPINDICATOR
        if entry.SSPIndicator in self.SSPIndicators: 
            # If it is, increment the count
            self.SSPIndicators[entry.SSPIndicator] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.SSPIndicators[entry.SSPIndicator] = 1
        ##DATERECEIVED
        if entry.dateReceived in self.dateReceiveds: 
            # If it is, increment the count
            self.dateReceiveds[entry.dateReceived] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.dateReceiveds[entry.dateReceived] = 1
        ##DECISIONDATE
        if entry.decisionDate in self.decisionDates: 
            # If it is, increment the count
            self.decisionDates[entry.decisionDate] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.decisionDates[entry.decisionDate] = 1
    
    def trimDigit(self, category, threshold):
        
        for applicant in self.applicants:
            if (self.applicants[applicant] < 150):
                self.removeApplicantsLater.append(applicant)
        
        for type in self.types:
            if (self.types[type] < 10):
                self.removeTypesLater.append(type)             
        
        for applicantIndex in self.removeApplicantsLater:
            del self.applicants[applicantIndex]
        
        for typeIndex in self.removeTypesLater:
            del self.types[typeIndex]
       
        
    def calcProperties(self):
        self.applicants = dict()
        self.types = dict()
        self.kNumbers = dict()
        self.SSPIndicators = dict()
        self.decisionDates = dict()
        self.dateReceiveds = dict()
        
        for entry in self.entryList:# Check if the item is already in the dictionary
            self.allocateVariables(entry)
        
        self.applicants = dict(sorted(self.applicants.items(), key=lambda item: item[1], reverse=False))
        self.types = dict(sorted(self.types.items(), key=lambda item: item[1], reverse=False))
        self.kNumbers = dict(sorted(self.kNumbers.items(), key=lambda item: item[1], reverse=False))
        self.SSPIndicators = dict(sorted(self.SSPIndicators.items(), key=lambda item: item[1], reverse=False))
        self.decisionDates = dict(sorted(self.decisionDates.items(), key=lambda item: item[1], reverse=False))
        self.dateReceiveds = dict(sorted(self.dateReceiveds.items(), key=lambda item: item[1], reverse=False))
        
        

