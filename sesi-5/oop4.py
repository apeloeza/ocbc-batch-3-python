class Dog:
    #class attribute
    species = "Canis Familiars"

    def __init__(self,name,age):
        # instance attribute
        self.name=name
        self.age=age

#instatiating
dog1 = Dog('miles',2)
dog2 = Dog('miley',3)
print(dog1.name,dog1.age,dog1.species)
print(dog2.name,dog2.age,dog2.species)

Buddy = Dog("Buddy", 20)
Miles = Dog("Miles", 21)
print(Buddy.name)