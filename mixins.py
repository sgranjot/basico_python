class PrintableMixin:
    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model


class PrintablePerson(Person, PrintableMixin):
    pass


class PrintableCar(Car, PrintableMixin):
    pass


person = PrintablePerson("Alice", 30)
car = PrintableCar("Toyota", "Camry")

print(person)
print(car)