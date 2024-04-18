

class Trimmer():
    
    def __init__(self, data):
        self.data = data
        self.removeLater = []
    
    def eval(self, trimString):
        trimParams = trimString.split(', ')
        
        if self.toPlural(trimParams[0].lower()) in dir(self.data):
            print("in selfdata")
            if (trimParams[1].isdigit()):
                self.trimDigit(int(trimParams[1]))
            else:
                if trimParams[1].lower() in getattr(self.data, self.toPlural(trimParams[0].lower())):
                    self.trimString(trimParams[1].lower)
                else:
                    print("Expected input <CATEGORY>, <CATEGORYVARIABLE | MINVALUE>")
            
    def trimDigit(self, trimParam):
        print("intrimDigit")
    
    def trimString(self, trimParam):
        for category in dir(self.data):
            for dataValue in getattr(self.data, category):
                if (getattr(getattr(self.data, category), dataValue) == trimParam):
                    self.removeLater.append(getattr(getattr(self.data, category), dataValue))

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
        
        
        print("intrimString")
        
    def toPlural(self, word):
        if word.endswith('y'):
            return word[:-1] + 'ies'
        elif word[-1] in ['s', 'x', 'z'] or word[-2:] in ['sh', 'ch']:
            return word + 'es'
        else:
            return word + 's'