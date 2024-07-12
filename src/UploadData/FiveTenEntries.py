# Collection of 510K entries 

from Pluralizer import Pluralizer
import numpy as np
class FiveTenEntries:
    # MIN_APPLICANTS_VALUE = 150
    DEFAULT_THRESHOLD = 0
    removeLater = set()
    # removeThresholdIndex = 0
    removeEntryIndex = set()
    
    def __init__(self):
        self.entryList = []
        self.clearDictionaries()
    
    # add a entry into the entryList (input an entry into the list)
    def add(self, entry):
        self.entryList.append(entry)
    
    # reset all dictionaries depending on current entries in the entryList(current Data set)
    def calcProperties(self):
        self.clearDictionaries()
        
        # Check if the item is already in the dictionary
        for entry in self.entryList:
            self.allocateVariables(entry)
        
        self.setDictionaries()
    
    # trim the data set based on a certain minimum or maximum digit parameter
    def trimDigit(self, category, threshold, maxMin):
        categories = Pluralizer.toPlural(category)
        numpyEntryList = np.array(self.entryList)
        if categories in dir(self):
            for item in getattr(self, categories):
                if(maxMin == "max"):
                    if (getattr(self, categories).get(item) > int(threshold)):
                        self.removeLater.add(item)
                else:
                    if (getattr(self, categories).get(item) < int(threshold)):
                        self.removeLater.add(item)
            
            for item in sorted(self.removeLater):
                
                # Find indices where 'item' is present in the 'category' attribute of elements
                indices = np.where([item in getattr(entry,category) for entry in numpyEntryList if item != ''])[0]
                
                # Append the found indices to self.removeEntryIndex
                for index in indices:
                    self.removeEntryIndex.add(index)
                indices = []
                del getattr(self, categories)[item]
            
            if (len(self.removeEntryIndex)):
                self.entryList = np.delete(numpyEntryList, np.array(list(self.removeEntryIndex)))
            self.removeEntryIndex = set()
            self.removeLater = set()
    
    # print all the keys in a certain dictionary
    def print(self, category):
        categories = Pluralizer.toPlural(category)
        if (~len(getattr(self, categories))):
             self.calcProperties()
        mydictionary = getattr(self, categories)
        for key in mydictionary:
            print(key)
     
    # clear all dictionaries
    def clearDictionaries(self):
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
    
    # set dictionaries to reflect the number of elements attributed to each unique key... 
    # result of allocate variables function
    def setDictionaries(self):
        self.applicants = dict(sorted(self.applicants.items(), key=lambda item: item[1], reverse=False))
        self.types = dict(sorted(self.types.items(), key=lambda item: item[1], reverse=False))
        self.kNumbers = dict(sorted(self.kNumbers.items(), key=lambda item: item[1], reverse=False))
        self.SSPIndicators = dict(sorted(self.SSPIndicators.items(), key=lambda item: item[1], reverse=False))
        self.decisionDates = dict(sorted(self.decisionDates.items(), key=lambda item: item[1], reverse=False))
        self.dateReceiveds = dict(sorted(self.dateReceiveds.items(), key=lambda item: item[1], reverse=False))
        self.contacts = dict(sorted(self.contacts.items(), key=lambda item: item[1], reverse=False))
        self.street1s = dict(sorted(self.street1s.items(), key=lambda item: item[1], reverse=False))
        self.street2s = dict(sorted(self.street2s.items(), key=lambda item: item[1], reverse=False))
        self.cities = dict(sorted(self.cities.items(), key=lambda item: item[1], reverse=False))
        self.states = dict(sorted(self.states.items(), key=lambda item: item[1], reverse=False))
        self.countryCodes = dict(sorted(self.countryCodes.items(), key=lambda item: item[1], reverse=False))
        self.zips = dict(sorted(self.zips.items(), key=lambda item: item[1], reverse=False))
        self.postalCodes = dict(sorted(self.postalCodes.items(), key=lambda item: item[1], reverse=False))
        self.decisions = dict(sorted(self.decisions.items(), key=lambda item: item[1], reverse=False))
        self.reviewAdviseComms = dict(sorted(self.reviewAdviseComms.items(), key=lambda item: item[1], reverse=False))
        self.productCodes = dict(sorted(self.productCodes.items(), key=lambda item: item[1], reverse=False))
        self.stateOrSumms = dict(sorted(self.stateOrSumms.items(), key=lambda item: item[1], reverse=False))
        self.classAdviceSumms = dict(sorted(self.classAdviceSumms.items(), key=lambda item: item[1], reverse=False))
        self.thirdParties = dict(sorted(self.thirdParties.items(), key=lambda item: item[1], reverse=False))
        self.expeditedReviews = dict(sorted(self.expeditedReviews.items(), key=lambda item: item[1], reverse=False))
        self.deviceNames = dict(sorted(self.deviceNames.items(), key=lambda item: item[1], reverse=False))
    
    # add up the number of occurences of each unique entry 
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
        #Contacts
        if entry.contact in self.contacts: 
            # If it is, increment the count
            self.contacts[entry.contact] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.contacts[entry.contact] = 1
        ## STREET1s  
        if entry.street1 in self.street1s: 
            # If it is, increment the count
            self.street1s[entry.street1] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.street1s[entry.street1] = 1
        ## STREET2s  
        if entry.street2 in self.street2s: 
            # If it is, increment the count
            self.street2s[entry.street2] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.street2s[entry.street2] = 1
        ##CITIES
        if entry.city in self.cities: 
            # If it is, increment the count
            self.cities[entry.city] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.cities[entry.city] = 1
        ##STATES
        if entry.state in self.states: 
            # If it is, increment the count
            self.states[entry.state] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.states[entry.state] = 1
        ##COUNTRYCODES
        if entry.countryCode in self.countryCodes: 
            # If it is, increment the count
            self.countryCodes[entry.countryCode] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.countryCodes[entry.countryCode] = 1
        ##ZIPS
        if entry.zip in self.zips: 
            # If it is, increment the count
            self.zips[entry.zip] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.zips[entry.zip] = 1
        ## POSTALCODES  
        if entry.postalCode in self.postalCodes: 
            # If it is, increment the count
            self.postalCodes[entry.postalCode] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.postalCodes[entry.postalCode] = 1
        ## DECISIONS  
        if entry.decision in self.decisions: 
            # If it is, increment the count
            self.decisions[entry.decision] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.decisions[entry.decision] = 1
        ##REVIEWADVISECOMMS
        if entry.reviewAdviseComm in self.reviewAdviseComms: 
            # If it is, increment the count
            self.reviewAdviseComms[entry.reviewAdviseComm] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.reviewAdviseComms[entry.reviewAdviseComm] = 1
        ##PRODUCTCODES
        if entry.productCode in self.productCodes: 
            # If it is, increment the count
            self.productCodes[entry.productCode] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.productCodes[entry.productCode] = 1
        ##STATEORSUMMS
        if entry.stateOrSumm in self.stateOrSumms: 
            # If it is, increment the count
            self.stateOrSumms[entry.stateOrSumm] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.stateOrSumms[entry.stateOrSumm] = 1
        ##CLASSADVICESUMMS
        if entry.classAdviceSumm in self.classAdviceSumms: 
            # If it is, increment the count
            self.classAdviceSumms[entry.classAdviceSumm] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.classAdviceSumms[entry.classAdviceSumm] = 1
        ##THIRDPARTIES
        if entry.thirdParty in self.thirdParties: 
            # If it is, increment the count
            self.thirdParties[entry.thirdParty] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.thirdParties[entry.thirdParty] = 1
        ##EXPEDITEDREVIEWS
        if entry.expeditedReview in self.expeditedReviews: 
            # If it is, increment the count
            self.expeditedReviews[entry.expeditedReview] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.expeditedReviews[entry.expeditedReview] = 1
        ##DEVICENAMES
        if entry.deviceName in self.deviceNames: 
            # If it is, increment the count
            self.deviceNames[entry.deviceName] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            self.deviceNames[entry.deviceName] = 1