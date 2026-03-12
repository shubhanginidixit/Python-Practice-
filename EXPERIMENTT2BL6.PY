# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")


# Child class
class Dog(Animal):
    # Method overriding
    def sound(self):
        print("Dog barks")


# Another child class
class Cat(Animal):
    # Method overriding
    def sound(self):
        print("Cat meows")


# Runtime polymorphism
a1 = Dog()
a2 = Cat()

a1.sound()   # Calls Dog's overridden method
a2.sound()   # Calls Cat's overridden method