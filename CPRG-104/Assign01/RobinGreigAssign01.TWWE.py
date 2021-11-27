# -*- coding: utf-8 -*-
"""

Class: CPRG-104
Instructor: Hamdy Ibrahim
Student: Robin Greig
Created on 2021/10/29 20:21:51
Filename: RobinGreigAssign01.TWWE.py

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
            if Zoo.animalCount == 2: # If 2 animals don't input any more
                print('Zoo is full of animals')
            elif Zoo.animalCount == 1: # Import second animal
                print('Animal Added')
                Zoo.animalCount += 1
                if isinstance(self.__name, Tiger):
                    Zoo.Animal2 = "Tiger"
                elif isinstance(self.__name, WildCat):
                    Zoo.Animal2 = "WildCat"
                else:
                    Zoo.Animal2 = "Wolf"
            elif Zoo.animalCount == 0: # Import first animal
                print('Animal Added')
                Zoo.animalCount += 1
                if isinstance(self.__name, Tiger):
                    Zoo.Animal1 = "Tiger"
                elif isinstance(self.__name, WildCat):
                    Zoo.Animal1 = "WildCat"
                else:
                    Zoo.Animal1 = "Wolf"
        if isinstance(self.__name, Bird): # Import bird
            if Zoo.birdCount > 0:
                print('Zoo is full of birds') # if 1 bird dont' add more
            else:
                print('Bird Added')
                Zoo.birdCount +=1
                if isinstance(self.__name, Eagle):
                    Zoo.Bird = "Eagle"
                else:
                    Zoo.Bird = "FlightBird"
    
    def looking(self):
        if Zoo.animalCount == 0 and Zoo.birdCount == 0:
            print('Zoo is empty') # if zoo is empty

        if Zoo.Animal1 == "Tiger" or Zoo.Animal2 == "Tiger":
            a = Tiger()
            print('\nNumber of hands: '+str(a.getNumHands())+', Number of legs: '+str(a.getNumLegs()))
            a.getAttribute1() # inherited from Felines class
            a.getAttribute5() # from Tiger class

        if Zoo.Animal1 == "WildCat" or Zoo.Animal2 == "WildCat":
            a = WildCat()
            print('\nNumber of hands: '+str(a.getNumHands())+', Number of legs: '+str(a.getNumLegs()))
            # getNumWings & getNumLegs inherited from Bird class
            a.getAttribute1() # inherited from Felines class
            a.getAttribute6() # from WildCats class
            
        if Zoo.Animal1 == "Wolf" or Zoo.Animal2 == "Wolf":
            a = Wolf()
            print('\nNumber of hands: '+str(a.getNumHands())+', Number of legs: '+str(a.getNumLegs()))
            # getNumHands & getNumLegs inherited from Animal class
            a.getAttribute3() # inherited from Canine class
            a.getAttribute4() # from Wolf class   
            
        if Zoo.Bird == "Eagle":
            a = Eagle()
            print('\nNumber of wings: '+str(a.getNumWings())+', Number of legs: '+str(a.getNumLegs()))
            # getNumWings & getNumLegs inherited from Bird class
            a.getAttribute7() # inherited from FlightBird class
            a.getAttribute8() # from Eagles class
        
        if Zoo.Bird == "FlightBird":
            a = FlightBird()
            print('\nNumber of wings: '+str(a.getNumWings())+', Number of legs: '+str(a.getNumLegs()))
            # getNumWings & getNumLegs inherited from Bird class
            a.getAttribute7() # inherited from FlightBird class
            

class Animal(Zoo):
    ''' This is the parent class for Canines & Felines '''

    __numLegs = 4 # Static Attribute set for number of legs of animals"
    __numHands = 0 # Static Attribute set for number of hands of animals"
    
    def __init__(self):
        Zoo.__init__(self)

    @staticmethod    
    def getNumLegs():
        return Animal.__numLegs

    @staticmethod    
    def getNumHands():
        return Animal.__numHands


class Feline(Animal):
    ''' This is the parent class for Eagles '''
    
    __attribute1 = "Felines belong to the cat family"
    __attribute2 = "Wild Cats & Tigers can climb trees"

    def __init__(self):
        Animal.__init__(self)

    @staticmethod
    def getAttribute1():
        print(Feline.__attribute1)
        
    def getAttribute2():
        print(Feline.__attribute2)

class Canine(Animal):
    ''' This is the parent class for Wolves '''
    
    __attribute3 = "Canines belong to the Dog family"
    

    def __init__(self):
        Animal.__init__(self)

    @staticmethod
    def getAttribute3():
        print(Canine.__attribute3)

class Wolf(Canine):
    ''' This is the class for Wolves '''
    
    __attribute4 = "Wolves hunt in packs and have a leader"

    def __init__(self):
        Animal.__init__(self)

    @staticmethod
    def getAttribute4():
        print(Wolf.__attribute4)


class Tiger(Feline):
    ''' This is the class for Tigers '''
    
    __attribute5 = "Tigers can roar and are lethal predators"

    def __init__(self):
        Animal.__init__(self)

    @staticmethod
    def getAttribute5():
        print(Tiger.__attribute5)
    
    def getTigerInfo():
        print(getAttribute5())

    
class WildCat(Feline):
    ''' This is the class for Wild Cats'''
    
    __attribute6 = "Wild Cats can climb trees"

    def __init__(self):
        Animal.__init__(self)

    @staticmethod
    def getAttribute6():
        print(WildCat.__attribute6)    

class Bird(Zoo):
    ''' This is the parent class for Flight Birds '''
    
    __numLegs = 2
    __numWings = 2

    def __init__(self):
        Zoo.__init__(self)
    
    @staticmethod    
    def getNumLegs():
        return Bird.__numLegs

    @staticmethod    
    def getNumWings():
        return Bird.__numWings


class FlightBird(Bird):
    ''' This is the parent class for Eagles '''
    
    __attribute7 = "Flight Birds fly and hunt for Food"

    def __init__(self):
        Bird.__init__(self)
        
    @staticmethod
    def getAttribute7():
        print(FlightBird.__attribute7)

class Eagle(FlightBird):
    ''' This is the class for Eagles '''
    
    __attribute8 = "Eagles fly extremely high and can see their prey from high up in the sky"

    def __init__(self):
        Bird.__init__(self)

    @staticmethod
    def getAttribute8():
        print(Eagle.__attribute8)

zoo=Zoo()
zoo.add(Tiger())
zoo.add(Wolf())
zoo.add(WildCat())
zoo.add(Eagle())
zoo.add(FlightBird())
zoo.looking()

