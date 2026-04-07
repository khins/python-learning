"""
Python classes and OOP: inheritance, properties, special methods, class/static methods.

Run this file to see examples and output.
"""

from typing import List, Iterator


class Animal:
    """Base class for animals."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def speak(self) -> str:
        return f"{self.name} makes a sound"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Animal):
            return NotImplemented
        return self.name == other.name and self.age == other.age


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
    """Person class with properties and methods."""

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self) -> str:
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, value: str):
        parts = value.split()
        if len(parts) != 2:
            raise ValueError("Full name must have exactly two parts")
        self._first_name, self._last_name = parts

    @classmethod
    def from_full_name(cls, full_name: str) -> 'Person':
        parts = full_name.split()
        if len(parts) != 2:
            raise ValueError("Full name must have exactly two parts")
        return cls(parts[0], parts[1])

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    def __repr__(self) -> str:
        return f"Person('{self.full_name}')"


class Playlist:
    """Playlist class with iteration support."""

    def __init__(self, songs: List[str]):
        self.songs = songs

    def __iter__(self) -> Iterator[str]:
        return iter(self.songs)

    def __len__(self) -> int:
        return len(self.songs)

    def __getitem__(self, index: int) -> str:
        return self.songs[index]


def run_demo() -> None:
    # Basic inheritance
    animal = Animal("Generic", 5)
    dog = Dog("Buddy", 3, "Golden Retriever")
    print('Animal:', animal)
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
