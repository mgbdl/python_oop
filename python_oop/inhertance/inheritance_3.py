åclass Contact:
    all_contacts = []
    hello = hello

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

# Python 3.7.2
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

# Python 2.7
# class Friend(Contact):
#     def __init__(self, name, email, phone):
#         Contact.__init__(self, name, email)
#         self.phone = phone

if __name__ == '__main__':
    f = Friend('John', 'john@gmail.com', '444-444-4444')
    print(f.name, f.email, f.phone)
    print(Contact.all_contacts)
