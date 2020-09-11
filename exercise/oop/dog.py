class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class JackRussellTerrier(Dog):
    pass


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass