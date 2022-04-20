#Object-Oriented Programming (OOP) in Python
# class Dog:
#     pass

#     def __init__(self, name, age):
#         self.name   = name
#         self.age    = age


    # def __init__(self, inputted_name, inputted_age):
    #     self.name   = inputted_name
    #     self.age    = inputted_age
    #     # self.name = 'Miles'
    #     # self.age = '4'

    
#Object-Oriented Programming (OOP) in Python
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

print('aman')

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print(buddy.name)
print(buddy.age)
print(buddy.species)

#instantiating
Dog('Miles',2)

#(pada pendefinisian class
# ada method )