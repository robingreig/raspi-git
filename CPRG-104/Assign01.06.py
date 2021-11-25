# -*- coding: utf-8 -*-
"""

Class: CPRG-104
Instructor: Hamdy Ibrahim
Student: Robin Greig
Created on 2021/10/28 19:02:01  
Filename: Assignment01.06.py

"""
class Zoo:
    ''' This is the parent class for both Animals & Birds'''
    
    animalCount = 0 # number of animals in the zoo
    birdCount = 0 # number of birds in the zoo
    
    #def __init__(self, name):
    def __init__(self):
        self.name = ''

#    def getName(self):
#        print('getName() called')
#        print(self.__name)
#        return self.__name

    def add(self, name):
        self.name = name
        print('add() called')
        print(self.name)
        self.name = Tiger()

#        print("Zoo Name = ",getName())
#        if Zoo.animalCount > 1:
#            print("Zoo full for Animals")
#        else:    
#            print("Animal Added")
#            Zoo.animalCount += 1
#            print("animalCount = ",Zoo.animalCount)

class Animal(Zoo):
    ''' This is the parent class for Canines & Felines '''

    __numLegs = 4 # Static Attribute set for number of legs of animals"
    __numHands = 0 # Static Attribute set for number of hands of animals"
    
    def __init__(self):
        Zoo.__init__(self)

    @staticmethod    
    def getNumLegs():
        print(Animal.__numLegs)


class Feline(Animal):
    ''' This is the parent class for Eagles '''
    
    __attribute1 = "Felines belong to the cat family"
    __attribute2 = "Wild Cats & Tigers can climb trees"

    def __init__(self):
        Animal.__init__(self)


class Canine(Animal):
    ''' This is the parent class for Wolves '''
    
    __attribute = "Canines belong to the Dog family"
    

    def __init__(self):
        Animal.__init__(self)


class Wolf(Canine):
    ''' This is the class for Wolves '''
    
    __attribute = "Wolves hunt in packs and have a leader"

    def __init__(self):
        Animal.__init__(self)

    @staticmethod
    def getAttribute():
        print(Wolf.__attribute)


class Tiger(Feline):
    ''' This is the class for Tigers '''
    
    __attribute1 = "Tigers can roar and are lethal predators"

    def __init__(self):
        Animal.__init__(self)

    @staticmethod
    def getAttribute1():
        print(Tiger.__attribute1)

    
class WildCat(Feline):
    ''' This is the class for Wild Cats'''
    
    __attribute = "Wild Cats can climb trees"

    def __init__(self):
        Animal.__init__(self)

    @staticmethod
    def getAttribute():
        print(WildCat.__attribute)    

class Bird(Zoo):
    ''' This is the parent class for Flight Birds '''
    
    __numLegs = 2
    __numWings = 2

    def __init__(self):
        Zoo.__init__(self)
    
    @staticmethod    
    def getNumLegs():
        print(Animal.__numLegs)

class FlightBird(Bird):
    ''' This is the parent class for Eagles '''
    
    __attribute1 = "Flight Birds fly and hunt for Food"

    def __init__(self):
        Bird.__init__(self)
        
    @staticmethod
    def getAttribute1():
        print(FlightBird.__attribute1)

class Eagle(FlightBird):
    ''' This is the class for Eagles '''
    
    __attribute = "Eagles fly extremely high and can see their prey from high up in the sky"

    def __init__(self):
        Bird.__init__(self)

    @staticmethod
    def getAttribute():
        print(Eagle.__attribute)

zoo=Zoo()
zoo.add(Tiger())
print(isinstance(Tiger, Zoo))
print(isinstance(Tiger, Animal))
print(isinstance(Tiger, Feline))
print(isinstance(Tiger, Tiger))
#print(zoo.getName())
#zoo.add(Wolf())
#Zoo.add(WildCat())
#Zoo.add(Eagle())
#WildCat.getAttribute()
#WildCat.getNumLegs()
#Eagle.getAttribute()
#FlightBird.getAttribute1()
#print(issubclass(Wolf, Canine))
#print(issubclass(Tiger, Feline))
#print(issubclass(Eagle, Bird))
