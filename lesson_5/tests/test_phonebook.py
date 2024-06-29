import unittest
from PhoneBook import PhoneBook

class TestPhoneBook(unittest.TestCase):
    # запускается перед каждым тестом.
    def setUp(self) -> None:
        self.phonebook = PhoneBook()
        return super().setUp()
    
    # запускается после каждого теста.
    def tearDown(self) -> None:
        del self.phonebook
        return super().tearDown()
    
    def test_create_new_phonebook(self):
        #phonebook = PhoneBook()
        self.assertEqual(0,len(self.phonebook.get_all_contacts()))

    def test_create_book(self):
        self.phonebook = PhoneBook()
        self.phonebook.add_contact("папа",1234)
        self.phonebook.add_contact("мама",12345)
        self.phonebook.add_contact("брат",1234)
        self.assertEqual(2, len(self.phonebook.get_all_contacts()))