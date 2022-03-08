from contacts import Contact
import unittest

class ContactTest(unittest.TestCase):
    def test_initialization(self):
        self.contact_x = Contact("Sylvestus", "sylvestus@gmail.com", "85688")
        self.assertTrue(isinstance(self.contact_x, Contact))


if __name__ == "__main__":
    unittest.main()