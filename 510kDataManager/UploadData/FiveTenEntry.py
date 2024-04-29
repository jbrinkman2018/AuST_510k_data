# Data stored into an in memory variable

# Jared Brinkman 3-26-24

class FiveTenEntry:
    def __init__(self, entryString):
        onData = entryString.split('|')
        self.dataArray = onData
        self.kNumber = onData[0].lower()
        self.applicant = onData[1].lower()
        self.contact = onData[2].lower()
        self.street1 = onData[3].lower()
        self.street2 = onData[4].lower()
        self.city = onData[5].lower()
        self.state = onData[6].lower()
        self.countryCode = onData[7].lower()
        self.zip = onData[8].lower()
        self.postalCode = onData[9].lower()
        self.dateReceived = onData[10].lower()
        self.decisionDate = onData[11].lower()
        self.decision = onData[12].lower()
        self.reviewAdviseComm = onData[13].lower()
        self.productCode = onData[14].lower()
        self.stateOrSumm = onData[15].lower()
        self.classAdviceSumm = onData[16].lower()
        self.SSPIndicator = onData[17].lower()
        self.type = onData[18].lower()
        self.thirdParty = onData[19].lower()
        self.expeditedReview = onData[20].lower()
        self.deviceName = onData[21].lower()
    def toArray(self):
        return self.dataArray