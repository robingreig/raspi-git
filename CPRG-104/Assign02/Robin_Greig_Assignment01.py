# -*- coding: utf-8 -*-
"""

Class: CPRG-104
Instructor: Hamdy Ibrahim
Student: Robin Greig
Created on 2021/11/19 15:33:21
Filename: Robin_Greig_Assignment02.py 

"""
# Import python modules
import functools
import re

class Fish:
    pass

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
        try:
            if isinstance(living_thing, Animal):
                if len(self.__animal_list) == 0:
                    self.__animal_list.append(living_thing)
                    print("First Animal Added")
                    if isinstance(living_thing, Tiger):
                        self.__zooAnimal1 = ['Tiger']
                    elif isinstance(living_thing, WildCat):
                        self.__zooAnimal1 = ['WildCat']
                    else:
                        self.__zooAnimal1 = ['Wolf']
                elif len(self.__animal_list) == 1:
                    if isinstance(living_thing, Tiger):
                        self.__zooAnimal2 = ['Tiger']
                    elif isinstance(living_thing, WildCat):
                        self.__zooAnimal2 = ['WildCat']
                    else:
                        self.__zooAnimal2 = ['Wolf']
                    tigerCheck = list(filter(lambda animal: animal == 'Tiger', self.__zooAnimal2))
                    wildCatCheck = list(filter(lambda animal: animal == 'WildCat', self.__zooAnimal2))
                    wolfCheck = list(filter(lambda animal: animal == 'Wolf', self.__zooAnimal2))
                    if self.__zooAnimal1 == tigerCheck or self.__zooAnimal1 == wildCatCheck or self.__zooAnimal1 == wolfCheck:
                        print(self.__zooAnimal1,'is already added once, cannot add a second time\n')
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
            elif not isinstance(living_thing, Animal) and not isinstance(living_thing, Bird):
                raise Exception
        except:
            print("\nThis living_thing: ",living_thing,"is not an Animal or Bird")
            print("Exception caught in 'except' step of try / except / else loop\n")
        else:
            print("Zoo successfully updated by try/except/else loop!\n")

    def looking(self):
        if len(self.__bird_list) == 0 and len(self.__animal_list) == 0:
            print("Zoo is empty")
        print('\n===Printing Zoo Listing===') # Original Zoo Listing from Assignment 1
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
        print('\n===Combined Single String===\n',list(prod)) # print combined string
        
    def findCanine(self):
        canineString = ''
        canineSet = list(map(lambda  animal: animal.look() , self.__animal_list)) # create list from map object of animals
        canineList = [x for x in canineSet if "Canines" in x] # use list of comprehension to filter for Wolves
        for a in canineList: # convert list to a string to preserve line formatting
            canineString += a
        print('\n===Canine Found===\n',canineString) # Print string containing a Canine
        
    def findTiger(self):
        for animal in self.__animal_list: # Loop thru to find tiger
            animalString = ''
            animalList = animal.look()
            for x in animalList: # Convert animalList into a string for regex
                animalString += x
            matchCheck = re.search("Tiger", animalString) # Use regex to find Tiger
            if matchCheck: # If Tiger is found in string, print it
                print('\n===Tiger Found===\n',animalString)
        

zoo = Zoo()
zoo.add(Fish())
zoo.add(Tiger())
zoo.add(Tiger())
zoo.add(Wolf())
zoo.add(Eagle())
zoo.looking()
zoo.findCanine()
zoo.findTiger()
