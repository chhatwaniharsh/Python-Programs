class Cat:
    def sound(self):
        print("Meow! Meow!")

class Dog:
    def sound(self):
        print("Boww! Boow!")

class Cow:
    def talk(self):
        print("Moww! Muww!")

class Goat:
    def sound(self):
        print("Meh! Mehh!")


def call(obj):
    if hasattr(obj,"sound"):
        obj.sound()
    elif hasattr(obj,"talk"):
        obj.talk()
    
li=[Cat(),Dog(),Cow(),Goat()]
for obj in li:
    call(obj)
