class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send"
                "{} order {}".format(order, self.name))

if __name__ == '__main__':
    c = Contact("Some Body", "somebody@example.net")
    s = Supplier("Some Body", "supplier@example.net")

    print(c.name, c.email, s.name, s.email)
    print(c.all_contacts)
    s.order("Ineed pliers")
