# class Contact:
#     all_contacts = []
#
#     def __init__(self, name='', email='', **kwargs):
#         super().__init__(**kwargs)
#         self.name = name
#         self.email = email
#         self.all_contacts.append(self)
#
# class AddressHolder:
#     def __init__(self, street='', city='', state='', code='', **kwargs):
#         super().__init__(**kwargs)
#         self.street = street
#         self.city = city
#         self.state = state
#         self.code = code
#
# class Friend(Contact, AddressHolder):
#     def __init__(self, phone='', **kwargs):
#         super().__init__(**kwargs)
#         self.phone = phone

class AddressHolder:
    def __init__(self, street='', city='', state='', code='', *args, **kwargs):
        print("{}\n args: {}\n kwargs: {}\n vars: {}".format('AddressHolder', args, kwargs, (street, city, state, code)))

        super().__init__(*args, **kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Contact:
    all_contacts = []

    def __init__(self, name='', email='', *args, **kwargs):
        print("{}\n args: {}\n kwargs: {}\n vars: {}".format('Contact', args, kwargs, (name, email)))

        super().__init__(*args, **kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class Friend(Contact, AddressHolder):

    # def greatings(self):
    #     print('Hi my name is {}'.format(self.name))

    def __init__(self, phone='', *args, **kwargs):
        print("{}\n args: {}\n kwargs: {}\n vars: {}".format('Friend', args, kwargs, (phone)))

        super().__init__(*args, **kwargs)
        self.phone = phone

if __name__ == '__main__':
    f = Friend(street="street", city='city', state='state', code='code', name='Mike', email='mike@gmail.com', phone="444-444-4444") # kwargs unorder
    # f = Friend('444-444-4444', 'Mike', 'mike@gmail.com', street="street", city='city', state='state', code='code') # kwargs unorder
    # f = Friend('444-444-4444', 'Mike', street="street", city='city', state='state', code='code', email='mike@gmail.com') # kwargs unorder
    # f = Friend('444-444-4444', 'name', 'email', 'street', 'city', 'state', 'code', other="other") # args Ordered variables
    print(f.phone, f.street, f.city, f.state, f.code, f.name, f.email)
    print(Contact.all_contacts)


# def test(name, *args, **kwargs):
#     print(name, args, kwargs)
#
# test('Mike', 'mundo', aux="aux")
