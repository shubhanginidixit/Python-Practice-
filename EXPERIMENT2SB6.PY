# Metaclass to enforce mandatory class attributes
class AttributeCheckMeta(type):
    def __new__(cls, name, bases, attrs):
        # Required class attributes
        required_attributes = ["name", "version"]

        for attr in required_attributes:
            if attr not in attrs:
                raise TypeError(f"Class '{name}' must define '{attr}' attribute")

        return super().__new__(cls, name, bases, attrs)


# Class using the metaclass
class MyFramework(metaclass=AttributeCheckMeta):
    name = "CustomFramework"
    version = "1.0"

    def show_info(self):
        print(f"{self.name} Version {self.version}")


# Object creation
obj = MyFramework()
obj.show_info()