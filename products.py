"""
    In this file we demonstrate two principles of OOP:

    # Encapsulation

    Encapsulation is the mechanism of restricting access to
    certain components of an object, hiding its internal state and
    requiring all interaction to be performed through well-defined interfaces (methods).

    ## Key Points:

    - Data Hiding: Internal data (attributes) is hidden from the outside world.
    - Access Control: Use public, private, or protected modifiers to control visibility.
    - Methods as Interfaces: Provide methods (getters/setters) to interact with the object's data.

    # Inheritance

    Inheritance allows a class (child/subclass) to inherit
    properties and behaviors (methods) from another class (parent/superclass).
    This promotes code reusability and hierarchical relationships.

    ## Key Points:

    - Base and Derived Classes: The parent class provides common functionality,
        while the child class extends or specializes it.
    - Method Overriding: Child classes can override parent class methods.
    - Types of Inheritance: Single, multiple, multilevel, hierarchical, and hybrid.

    # Polymorphism

    Polymorphism allows objects of different classes to be treated through a common interface,
    enabling a single action to behave differently depending on the object performing it.
    It promotes flexibility and extensibility in object-oriented design.

    ## Key Points
    - Method Overriding: Child classes provide their own implementation
        of a method defined in the parent class, allowing behavior to vary.
    - Method Overloading: Multiple methods share the same name but differ in parameters
    - Dynamic Dispatch: The method that gets executed is determined at runtime
        based on the actual object type.
    - Common Interfaces: Different classes implement the same interface,
        enabling interchangeable use.Abstraction

    # Abstraction

    Abstraction is the principle of exposing only the essential features of an object
    while hiding unnecessary implementation details.
    It simplifies complexity by focusing on what an object does rather than how it does it.

    ## Key Points

    - Essential Behavior Only: Shows only relevant operations to the user while hiding internal logic.
    - Abstract Classes: Provide a base structure with incomplete methods that subclasses must implement.
    - Interfaces as Contracts: Define a set of methods that implementing classes must provide.
    - Reduced Complexity: Helps manage large systems by separating high-level operations from low-level details.

"""
from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            raise ValueError("Product price has been updated to a negative value")

    # getter
    def get_price(self):
        return self.__price

    @abstractmethod
    def total_price(self, quantity):
        pass

class PhysicalProduct(Product):

    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def __str__(self):
        return f" Product '{self.name}'"

    def total_price(self, quantity):
        return self.get_price() * quantity + self.weight / 1000 * 10

class DigitalProduct(Product):

    def __init__(self, name, price, link):
        super().__init__(name, price)
        self.link = link

    def total_price(self, quantity):
        return self.get_price() * quantity

class SubscriptionProduct(DigitalProduct):

    def __init__(self, name, price, link):
        super().__init__(name, price, link)

if __name__ == '__main__':
    product = PhysicalProduct(name = "teacup", price = 10, weight = 300)
    print(product)
    print(product.name)
    print(product.get_price())
