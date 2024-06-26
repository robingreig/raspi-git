# -*- coding: utf-8 -*-
"""

Class: CPRG-104
Instructor: Hamdy Ibrahim
Student: Robin Greig
Created on 2021/11/24 15:33:21
Filename: Assignment02.00.py 

"""
import functools

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
        
    def add(self, living_thing):
        try:
            if isinstance(living_thing, Animal):
                if len(self.__animal_list) == 0:
                    self.__animal_list.append(living_thing)
                    print("Animal Added")
                    if isinstance(living_thing, Tiger):
                        zooAnimal1 = ['Tiger']
                        print('Tiger added to animals')
                    elif isinstance(living_thing, WildCat):
                        zooAnimal1 = ['WildCat']
                        print('WildCat added to animals')
                    else:
                        zooAnimal1 = ['Wolf']
                        print('Wolf added to animals')
                    print('First Animal Added')
                elif len(self.__animal_list) == 1:
                    if filter(living_thing, zooAnimal1):
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
            else:
                print('Not an animal or a bird')
        except:
            print("This animal is already in the zoo, cannot be added again")
        else:
            print('living thing successfully added')
    def looking(self):
        if len(self.__bird_list) == 0 and len(self.__animal_list) == 0:
            print("Zoo is empty")
        for animal in self.__animal_list:
            print(animal.look())
            print("")
        for bird in self.__bird_list:
            print(bird.look())
            print("")
                
zoo = Zoo()
zoo.add(Fish())
#zoo.add(Tiger())
#zoo.add(Wolf())
#zoo.add(WildCat())
#zoo.add(Eagle())
zoo.looking()
