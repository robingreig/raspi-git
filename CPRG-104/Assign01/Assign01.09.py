# -*- coding: utf-8 -*-
"""

Class: CPRG-104
Instructor: Hamdy Ibrahim
Student: Robin Greig
Created on 2021/10/29 13:44:14  
Filename: Assignment02.05.py

"""
class Zoo:
    ''' This is the parent class for both Animals & Birds'''
    
    animalCount = 0 # number of animals in the zoo
    birdCount = 0 # number of birds in the zoo
    Animal1 = '' # type of first animal in zoo
    Animal2 = '' # type of second animal in zoo
    Bird = '' # type of bird in zoo
    
    def __init__(self):
        self.__name = ''

    def add(self, name):
        self.__name = name
        if isinstance(self.__name, Animal):
            if Zoo.animalCount == 2:
                print('Zoo is full of animals')
            elif Zoo.animalCount == 1:
                print('Animal Added')
                Zoo.animalCount += 1
                if isinstance(self.__name, Tiger):
                    Zoo.Animal2 = "Tiger"
                elif isinstance(self.__name, WildCat):
                    Zoo.Animal2 = "WildCat"
                else:
                    Zoo.Animal2 = "Wolf"
                print('Zoo.Animal2: '+Zoo.Animal2)
            elif Zoo.animalCount == 0:
                print('Animal Added')
                Zoo.animalCount += 1
                if isinstance(self.__name, Tiger):
                    Zoo.Animal1 = "Tiger"
                elif isinstance(self.__name, WildCat):
                    Zoo.Animal1 = "WildCat"
                else:
                    Zoo.Animal1 = "Wolf"
                print('Zoo.Animal1: '+Zoo.Animal1)
        if isinstance(self.__name, Bird):
            if Zoo.birdCount > 0:
                print('Zoo is full of birds')
            else:
                print('Bird Added')
                Zoo.birdCount +=1
                if isinstance(self.__name, Eagle):
                    Zoo.Bird = "Eagle"
                else:
                    Zoo.Bird = "FlightBird"
    
    def looking(self):
        print('Running looking()')
        print('Zoo.animalCount: '+str(Zoo.animalCount))
        if Zoo.animalCount == 0 and Zoo.birdCount == 0:
            print('Zoo is empty')
        elif Zoo.animalCount == 1:
            print('Zoo has 1 animal and it is a '+Zoo.Animal1)
        else:
            print('zooAnimal1: '+Zoo.Animal1)
            print('zooAnima12: '+Zoo.Animal2)
        if Zoo.birdCount > 0:
            print('Zoo has a bird and it is a '+Zoo.Bird)


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
zoo.add(Wolf())
zoo.add(WildCat())
zoo.add(Eagle())
zoo.looking()

#WildCat.getAttribute()
Tiger.getNumLegs()
#Eagle.getAttribute()
#FlightBird.getAttribute1()
