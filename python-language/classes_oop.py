"""
Python classes and OOP: inheritance, properties, special methods, class/static methods.

Run this file to see examples and output.
a compact OOP practice file that teaches four big ideas: inheritance,
 properties, special methods, and class/static methods.

Key idea: a class is a blueprint, and __init__ runs when you create 
an object like Animal("Generic", 5). 

Most important concepts to remember

A class is a blueprint; an object is an instance.
__init__ initializes object state.
Inheritance lets one class reuse another.
super() calls parent-class logic.
Overriding means redefining a parent method in a child class.
Properties let methods act like attributes.
Class methods are alternative constructors or class-level utilities.
Static methods are utility functions grouped inside a class.
Special methods like __repr__, __len__, and __getitem__ let custom 
classes integrate with Python syntax.
"""

from typing import List, Iterator

"""
Big Picture
The file builds three small examples:

Animal and Dog show inheritance and method overriding.
Person shows controlled attribute access with a property,
 plus @classmethod and @staticmethod.
Playlist shows how special methods let your objects behave like
 built-in Python containers.
"""
class Animal:
    """Base class for animals.
    1. Animal: the base class
 Animal defines shared data and behavior.

__init__ sets up each object with name and age.
speak() is a normal instance method.
__repr__() controls how the object prints in the console.
__eq__() controls how == works.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def speak(self) -> str:
        return f"{self.name} makes a sound"

    """
    Important detail:
__repr__ uses self.__class__.__name__, so it prints the actual class 
name of the object. That is a nice OOP touch because subclasses can
inherit it and still show their own type name.
    """
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Animal):
            return NotImplemented
        return self.name == other.name and self.age == other.age

"""
2. Dog(Animal): inheritance
In classes_oop.py (line 29), Dog inherits from Animal.

class Dog(Animal): means Dog gets Animal’s attributes and methods.
super().__init__(name, age) reuses the parent constructor.
self.breed = breed adds Dog-specific data.
speak() is overridden, so dogs bark instead of using the generic 
animal sound.
"""
class Dog(Animal):
    """Dog inherits from Animal."""

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> str:
        return f"{self.name} barks"

    def __repr__(self) -> str:
        return f"Dog(name='{self.name}', age={self.age}, breed='{self.breed}')"


class Person:
    """Person class with properties and methods.
    3. Person: properties and method types
    In classes_oop.py (line 43), Person introduces a few important
    Python patterns.

__init__

Stores _first_name and _last_name.
The leading underscore signals “internal use” by convention.
    """

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    """
    @property

    full_name looks like an attribute when accessed: person.full_name
    But it actually runs a method behind the scenes
    This is one of the most important lessons in the file: properties 
    let you protect and manage data without forcing clunky method calls
    like set_full_name().
    """
    @property
    def full_name(self) -> str:
        return f"{self._first_name} {self._last_name}"

    """
    Why this matters:
    You get a clean interface for the user of the class, 
    while still keeping logic inside the class.

    @full_name.setter

    Lets you assign with person.full_name = "Jane Smith"
    Validates the input before changing internal state
    Raises ValueError if the name does not have exactly two parts

    """
    @full_name.setter
    def full_name(self, value: str):
        parts = value.split()
        if len(parts) != 2:
            raise ValueError("Full name must have exactly two parts")
        self._first_name, self._last_name = parts

    """Why cls matters:
    If this class were subclassed later, the class method would still 
    create the subclass, not always a plain Person."""
    @classmethod
    def from_full_name(cls, full_name: str) -> 'Person':
        parts = full_name.split()
        if len(parts) != 2:
            raise ValueError("Full name must have exactly two parts")
        return cls(parts[0], parts[1])

    """@staticmethod

    is_adult(age)
    Does not need self or cls
    Belongs conceptually to Person, but does not use object or 
    class state"""
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    """Rule of thumb:

        Instance method: needs self
        Class method: needs cls
        Static method: needs neither"""
    def __repr__(self) -> str:
        return f"Person('{self.full_name}')"

"""4. Playlist: making custom objects feel built-in
In classes_oop.py (line 76), Playlist wraps a list of songs.

It defines:

__iter__() so you can loop over it
__len__() so len(playlist) works
__getitem__() so playlist[0] works
This is a powerful OOP technique: by implementing special methods, 
you can
"""
class Playlist:
    """Playlist class with iteration support.
    This is a great example of Python data model methods. 
    By implementing these “dunder methods,” your own classes 
    can behave like native types.

    So this works naturally:

    len(playlist)
    playlist[0]
    list(playlist)
    """

    def __init__(self, songs: List[str]):
        self.songs = songs

    def __iter__(self) -> Iterator[str]:
        return iter(self.songs)

    def __len__(self) -> int:
        return len(self.songs)

    def __getitem__(self, index: int) -> str:
        return self.songs[index]

"""
run_demo() ties everything together by creating 
objects and printing what they do.
5. What run_demo() is teaching
In the file demonstrates each concept 
in action.

Animal and Dog print differently because of __repr__
Dog.speak() overrides Animal.speak()
animal == dog is False because name and age differ
Person.full_name behaves like a managed attribute
Person.from_full_name(...) creates an object cleanly
Playlist acts like a sequence

"""
def run_demo() -> None:
    # Basic inheritance
    animal = Animal("Generic", 5)
    dog = Dog("Buddy", 3, "Golden Retriever")
    print('Animal:', animal)
    """
    Key idea: inheritance lets you reuse common code and customize
    only what changes.

    This is why:

    dog.name and dog.age still exist
    dog.speak() behaves differently from animal.speak()
    That is called polymorphism: same method name, different behavior
    depending on the object type.
    """
    print('Dog:', dog)
    print('Animal speak:', animal.speak())
    print('Dog speak:', dog.speak())
    print('Are equal?', animal == dog)

    # Properties
    person = Person("John", "Doe")
    print('Person:', person)
    print('Full name:', person.full_name)
    person.full_name = "Jane Smith"
    print('Updated person:', person)

    # Class method
    person2 = Person.from_full_name("Alice Johnson")
    print('From full name:', person2)

    # Static method
    print('Is adult (20)?', Person.is_adult(20))
    print('Is adult (15)?', Person.is_adult(15))

    # Iteration
    playlist = Playlist(["Song1", "Song2", "Song3"])
    print('Playlist length:', len(playlist))
    print('First song:', playlist[0])
    print('All songs:', list(playlist))


if __name__ == '__main__':
    run_demo()
