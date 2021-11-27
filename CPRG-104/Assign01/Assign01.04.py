# -*- coding: utf-8 -*-
"""

Class: CPRG-104
Instructor: Hamdy Ibrahim
Student: Robin Greig
Created on 2021/10/28 14:56:54
Filename: Assignment02.01.py 

"""

class animal:
    def __init__(self, name):
        self.__name = name
        self.__numLegs = 4
        self.__numHands = 0
    
    def walk(self):
        return self.__numLegs
    
    def run(self):
        print(self.__name+" is running")
        
    def getName(self):
        print(self.__name)
    
    def getName1(self):
        return self.__name

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name)
        self.breed = breed
    
    def bark(self):
        print("Dog is barking")
        
    
joe = dog("Joe","Spaniel")
joe.getName()
joe.run()
joe.walk()
print("Joe the ",joe.breed," has ",joe.walk()," legs")
print("Joe's name is ",joe.getName1())

