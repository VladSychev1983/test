class PhoneBook:
    def __init__(self, contacts=None):
        if contacts is None:
            contacts = {}
        self.contacts = contacts

    def add_contact(self, name, phone):
        if phone in self.contacts.values():
            return
        self.contacts[name.lower()] = phone

    def get_contact(self, name):
        return self.contacts.get(name.lower(), 'Телефон не известен')

    def get_all_contacts(self):
        return self.contacts

