# Inherith from built-ins

class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value
        in their name.'''
        return [contact for contact in self if name in contact.name]

class Contact():
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        return [key for key in self if not longest or len(key) > len(longest)][0]

if __name__ == '__main__':
    c1 = Contact("John A", "johna@example.net")
    c2 = Contact("John B", "johnb@example.net")
    c3 = Contact("Jenna C", "jenna@example.net")
    print([c.name for c in Contact.all_contacts.search('John')])

    longkeys = LongNameDict()
    longkeys['hello'] = 1
    longkeys['longest yet'] = 5
    longkeys['hello2'] = 'world'
    print(longkeys.longest_key())
