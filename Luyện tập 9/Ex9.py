class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print(self.name, "says: Gâu gâu")
d = Dog("Lucky")
d.sound()
