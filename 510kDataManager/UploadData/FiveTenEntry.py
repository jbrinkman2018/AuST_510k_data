# Data stored into an in memory variable

# Jared Brinkman 3-26-24

class FiveTenEntry:
    def __init__(self, entryString):
        onData = entryString.split('|')
        self.kNumber = onData[0]
        self.applicant = onData[1].lower()
        self.contact = onData[2]
        self.street1 = onData[3]
        self.street2 = onData[4]
        self.city = onData[5]
        self.state = onData[6]
        self.countryCode = onData[7]
        self.zip = onData[8]
        self.postalCode = onData[9]
        self.dateReceived = onData[10]
        self.decisionDate = onData[11]
        self.decision = onData[12]
        self.reviewAdviseComm = onData[13]
        self.productCode = onData[14]
        self.stateOrSumm = onData[15]
        self.classAdviceSumm = onData[16]
        self.SSPIndicator = onData[17]
        self.type = onData[18]
        self.thirdParty = onData[19]
        self.expeditedReview = onData[20]
        self.deviceName = onData[21]