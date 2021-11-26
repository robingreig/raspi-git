# -*- coding: utf-8 -*-
"""

Class: CPRG-104
Instructor: Hamdy Ibrahim
Student: Robin Greig
Created on 2021/11/19 15:33:21
Filename: Assignment02.01.py 

"""
# Import python modules
import functools
import re

class Animal:
    def __init__(self):
        self.__numLegs = 4
        self.__numHands = 0
    
    def look(self):
        return "Number of hands: {hand}, Number of legs: {leg}".format(hand=self.__numHands, leg=self.__numLegs)

class Bird:
    def __init__(self):
        self.__numLegs = 2
        self.__numWings = 2
    
    def look(self):
        return "number of wings: {wing}, Number of legs: {leg})".format(wing=self.__numWings, leg=self.__numLegs)

class Feline(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.__characteristic = "Felines belong to the cat family"
        
    def look(self):
        return super().look() + "\n" + self.get_characteristic()
        
    def get_characteristic(self):
        return self.__characteristic
        
class Tiger(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.__characteristic = "Tigers can roar and are lethal predators"
        
    def get_characteristic(self):
        return super().get_characteristic() + "\n" + self.__characteristic
        
class WildCat(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.__characteristic = "WildCats can climb trees"
        
    def get_characteristic(self):
        return super().get_characteristic() + "\n" + self.__characteristic
        
        
class Canine(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.__characteristic = "Canines belong to the dog family"
        
    def look(self):
        return super().look() + "\n" + self.get_characteristic()
        
    def get_characteristic(self):
        return self.__characteristic
        
class Wolf(Canine):
    def __init__(self):
        Canine.__init__(self)
        self.__characteristic = "Wolves hunt in packs and have a leader"
        
    def get_characteristic(self):
        return super().get_characteristic() + "\n" + self.__characteristic
        
class FlightBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.__characteristic = "Flight Birds fly and hunt for food"
        
    def look(self):
        return super().look() + "\n" + self.get_characteristic()
        
    def get_characteristic(self):
        return self.__characteristic

class Eagle(FlightBird):
    def __init__(self):
        FlightBird.__init__(self)
        self.__characteristic = "Eagles fly extremely high and can see their prey"
        
    def get_characteristic(self):
        return super().get_characteristic() + "\n" + self.__characteristic
        
class Zoo:
    def __init__(self):
        self.__animal_list = list()
        self.__bird_list = list()
        self.__zooAnimal1 = list()
        self.__zooAnimal2 = list()
        self.__zooString = list()
        
    def add(self, living_thing):
        if not isinstance(living_thing, Animal) and not isinstance(living_thing, Bird):
            raise Exception ("This is not animals or birds")
        try:
            if isinstance(living_thing, Animal):
                if len(self.__animal_list) == 0:
                    self.__animal_list.append(living_thing)
                    print("First Animal Added")
                    if isinstance(living_thing, Tiger):
                        self.__zooAnimal1 = ['Tiger']
                        print('Tiger added to animals')
                    elif isinstance(living_thing, WildCat):
                        self.__zooAnimal1 = ['WildCat']
                        print('WildCat added to animals')
                    else:
                        self.__zooAnimal1 = ['Wolf']
                        print('Wolf added to animals')
                    print('zooAnimal1 at end of if statement = ',self.__zooAnimal1)
                elif len(self.__animal_list) == 1:
                    print('zooAnimal1 at beginning of elif statement = ',self.__zooAnimal1)
                    if isinstance(living_thing, Tiger):
                        self.__zooAnimal2 = ['Tiger']
                        print('Tiger added to animals2')
                    elif isinstance(living_thing, WildCat):
                        self.__zooAnimal2 = ['WildCat']
                        print('WildCat added to animals2')
                    else:
                        self.__zooAnimal2 = ['Wolf']
                        print('Wolf added to animals2')
                    tigerCheck = list(filter(lambda animal: animal == 'Tiger', self.__zooAnimal2))
                    wildCatCheck = list(filter(lambda animal: animal == 'WildCat', self.__zooAnimal2))
                    wolfCheck = list(filter(lambda animal: animal == 'Wolf', self.__zooAnimal2))
                    if self.__zooAnimal1 == tigerCheck or self.__zooAnimal1 == wildCatCheck or self.__zooAnimal1 == wolfCheck:
                        print('Animal already added once, cannot add a second time')
                        return
                    self.__animal_list.append(living_thing)
                    print("Second Animal Added")
                else:
                    print("Zoo is full for animals")
            elif isinstance(living_thing, Bird):
                if len(self.__bird_list) < 1:
                    self.__bird_list.append(living_thing)
                    print("Bird Added")
                else:
                    print("Zoo is full for Birds")
        except:
            print("Exception has been raised in try/except/else")
        else:
            print("Zoo successfully updated by try/except/else\n")

    def looking(self):
        if len(self.__bird_list) == 0 and len(self.__animal_list) == 0:
            print("Zoo is empty")
        for animal in self.__animal_list:
            print(animal.look())
            print("")
        for bird in self.__bird_list:
            print(bird.look())
            print("")
        zooAnimals = list(map(lambda animal: animal.look(), self.__animal_list)) # create list from map object of animals
        zooBirds = list(map(lambda bird: bird.look(), self.__bird_list)) # create list from map object of bird
        self.__zooString.append(zooAnimals) # append zooAnimals to full zoo string
        self.__zooString.append(zooBirds) # append zooBirds to full zoo string
        prod = functools.reduce(lambda a,b: a+b, self.__zooString) # combine both strings using reduce
        print('Combined Single String:\n',list(prod)) # print combined string
        
    def canineLooking(self):
        canineSet = list(map(lambda  animal: animal.look() , self.__animal_list)) # create list from map object of animals
        canineList = functools.reduce(lambda a,b: b, canineSet)
        print('\ncanine Looking Method:\n',canineList)
        
    def filterTiger(self):
        zooAnimals = str(map(lambda animal: animal.look(), self.__animal_list)) # create list from map object of animals
        print(zooAnimals)
        matchSearch = re.search("cat", zooAnimals)
        print(matchSearch.span())

        




                
zoo = Zoo()
zoo.add(Tiger())
#zoo.add(Tiger())
zoo.add(Wolf())
#zoo.add(WildCat())
#zoo.add(Eagle())
#zoo.looking()
#zoo.canineLooking()
zoo.filterTiger()
