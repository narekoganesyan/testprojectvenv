class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split('-')
        return cls(name, int(age))

person = Person.from_string("John-25")
print(person.name, person.age)  # Output: John 25
