'''
we create a class
we add properties
we add methods

To create a contact application
we need:
-name
-email
-phone_numer

classmethod
property
instancemethod
'''

class Contact:
    contact_list = []
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    @property
    def print_name(self):
        return self.name

    @classmethod
    def save_contact(cls):
        cls.contact_list.append(7)

contact_x = Contact("Sylvestus", "sylvestus@gmail.com", "85688")


print(contact_x.print_name)