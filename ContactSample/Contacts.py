# Requirements
# ---------------

# First name
# Last name
# Email address
# Phone number
# physical address
# Company

# Which kind of actions would you perform with your application

# Add new contact - 
# Display the contacts
# Delete a contact
# Update a contact
# Copy the contact

# C
# R
# U
# D

class Contact:

    def __init__(self, first_name, last_name, email, phone_number, physical_address, company):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.physical_address = physical_address
        self.company = company

new_contact = Contact("Kelvin", "Irungu","kelvIr@gmail.com", "076548837", "Nairoi", "Moringa")
print(new_contact.first_name)
print(new_contact.last_name)
print(new_contact.email)
print(new_contact.__dict__)