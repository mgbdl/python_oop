# More Losely Coupled Design. When we known which is the final class
class BaseClass:
    num_base_calls = 0
    def __init__(self):
        print("Calling method on Base Class")
        self.num_base_calls +=1

class LeftSubclass:
    num_left_calls = 0
    def __init__(self):
        super().__init__()
        print("Calling method on Left Subclass")
        self.num_left_calls +=1

class RightSubclass:
    num_right_calls = 0
    def __init__(self):
        super().__init__()
        print("Calling method on Right Subclass")
        self.num_right_calls +=1

class Subclass(LeftSubclass, RightSubclass, BaseClass):
    num_subclass_calls = 0
    def call_me(self):
        print("Calling method on Subclass")
        self.num_subclass_calls +=1

# Less Tightly Coupled Design
class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls +=1


class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_calls +=1


class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls +=1

class Subclass(LeftSubclass, RightSubclass):
    num_subclass_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_subclass_calls +=1

if __name__ == '__main__':
    s = Subclass()
    s.call_me()
