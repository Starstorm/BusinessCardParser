class BusinessCardParser(object):
    def __init__(self):
        self.phone_regex = '(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'
        self.email_regex = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        self.name_db = names_dataset.NameDataset()
        self.name_ner = spacy.load('en_core_web_sm')
        
    def getContactInfo(self, document):
        name = self.extractName(document)
        email, phone = self.extratEmailPhone(document)
        return ContactInfo(name, phone, email)
    
    def extractName(self, document):
        name = "UNKNOWN"
        entities = self.name_ner(document)
        people = [str(elem) for elem in entities.ents if elem.label_ == "PERSON" and str(elem).count(" ") > 0]
        if len(people) == 1:
            name = people[0].replace("\n","").strip()
        elif len(people) > 1:
            for person in people:
                first_name = person.split()[0].strip()
                if self.name_db.search_first_name(first_name):
                    name = person
                    break
        return name
    
    def extractEmailPhone(self, document):
        email = "UNKNOWN"
        phone = "UNKNOWN"
        document_lines = document.split("\n")
        for line in document_lines:
            phone_re = re.search(self.phone_regex,line)
            email_re = re.search(self.email_regex,line)
            if phone_re and phone == "UNKNOWN" and not line.startswith(("Fax","fax","FAX")):
                raw_phone_number = phone_re.group().strip()
                phone = re.sub('[^0-9]','', raw_phone_number)
            if email_re and email == "UNKNOWN":
                email = email_re.group().strip()
        return email, phone

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
    
if __name__ == '__main__':
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True, help="Business card text file")
    ap.add_argument("-o", "--output", help="Output text for file. If not used, will display to screen.")
    my_args = vars(ap.parse_args())

    my_parser = BusinessCardParser()
    with open(my_args['file'],"r") as card_file:
        document = card_file.read()
    my_contact_info = my_parser.getConactInfo(document)
    if my_args['output']:
        with open(my_args['output'], "w") as output_file:
            output_file.write(my_contact_info.getName())
            output_file.write(my_contact_info.getEmail())
            output_file.write(my_contact_info.getPhone())
    else:
        print(my_contact_info.getName())
        print(my_contact_info.getEmail())
        print(my_contact_info.getPhone())
    
    
