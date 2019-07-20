import random

class Character:
    def __init__(self, name='', *args, **kwargs):
        if not name:
            raise ValueError('name is required')

        print("{}\n args: {}\n kwargs: {}".format('Character', args, kwargs))
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

class Sneaky:
    sneaky = True

    def __init__(self, sneaky=True, *args, **kwargs):
        print("{}\n args: {}\n kwargs: {}".format('Sneaky', args, kwargs))

        super().__init__(*args, **kwargs)
        self.sneaky = sneaky

    def hide(self, light_level):
        return self.sneaky and light_level < 10

class Agile:
    agile = True

    def __init__(self, agile=True, *args, **kwargs):
        print("{}\n args: {}\n kwargs: {}".format('Agile', args, kwargs))

        super().__init__(*args, **kwargs)
        self.agile = agile

    def evade(self):
        return self.agile and random.randint(0, 1)


class Thief(Agile, Sneaky, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))

if __name__ == '__main__':
    # t = Thief(name='Mike', sneaky=False, agile=False, other='other') #Kwargs unordered
    t = Thief(True, True, 'Mike', other='other') #Args ordered
    print("name: {}, sneaky: {}, agile: {}, hide: {}, evade: {}, other: {}".format(t.name, t.sneaky, t.agile, t.hide(8), t.evade(), t.other))
