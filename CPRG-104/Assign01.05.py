# -*- coding: utf-8 -*-
"""

Class: CPRG-104
Instructor: Hamdy Ibrahim
Student: Robin Greig
Created on 2021/10/28 16:05:18
Filename: Assignment01.05.py

"""
class Zoo:
    def __init__(self, name):
        self.__name = name
        
    def getName(self):
        print(self.__name)
        
    def getName1(self):
        return(self.__name)
    
class Animal(Zoo):
    
    __numLegs = 4
    __numHands = 0
    
    def __init__(self, name):
        Zoo.__init__(self, name)
        self.__name = name
        
    def walk(self):
        return self.__numLegs
    
    def run(self):
        print(self.__name+" is running")
    
    @staticmethod    
    def getNumLegs():
        return Animal.__numLegs
        
    def add(self):
        print("Animal Added")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        Zoo.__init__(self, name)
        self.breed = breed
    
#    def bark(self):
#        print("Dog is barking")
        
#animal.add(Tiger())    
joe = Dog("Joe","Spaniel")
joe.getName()
joe.run()
print("Joe the ",joe.breed," has ",joe.getNumLegs()," legs")
print("Joe's name is ",joe.getName1())
print("Joe has",joe.getNumLegs(),"legs")

