#instance method
class Person:
    def __init__(self, firstName, lastName, age):
        self.first = firstName
        self.last = lastName
        self.age = age
    #TODO: a method that return full name
    def fullName(self):
        return f"{self.first} {self.last}"

#object
o1 = Person('Peeyush','misra',19)

print(o1.fullName())