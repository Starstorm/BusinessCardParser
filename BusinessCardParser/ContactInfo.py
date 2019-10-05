class ContactInfo(object):
    def __init__(self, name, phone_number, email_address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        
    def __str__(self):
        return "Name: " + self.name + "\nPhone: " + self.phone_number + "\nEmail: " + self.email_address
    
    def getName(self):
        return self.name
    
    def getPhoneNumber(self):
        return self.name
    
    def getEmailAddress(self):
        return self.email_address
