# -*- coding: utf-8 -*-
"""

Class: CPRG-104
Instructor: Hamdy Ibrahim
Student: Robin Greig
Created on 2021/10/28 16:05:18
Filename: Assignment02.03.py

"""
class Zoo:
    
    animalCount = 0 # number of animals in the zoo
    
    #def __init__(self, name):
    def __init__(self):
        pass
        #self.__init__(self)
        #self.__name = name
        
#    def getName(self):
#        print(self.__name)
        
#    def getName1(self):
#        return(self.__name)


    def add(self):
        if Zoo.animalCount > 1:
            print("Zoo full for Animals")
        else:    
            print("Animal Added")
            Zoo.animalCount += 1
            print("animalCount = ",Zoo.animalCount)



class Animal(Zoo):
    
    __numLegs = 4
    __numHands = 0
    
    #def __init__(self, name):
    def __init__(self):
        #Zoo.__init__(self, name)
        Zoo.__init__(self)
        #self.__name = name
        
    def walk(self):
        return self.__numLegs
    
#    def run(self):
#        print(self.__name+" is running")
    
    @staticmethod    
    def getNumLegs():
        #return Animal.__numLegs
        print(Animal.__numLegs)


class Feline(Animal):
    #def __init__(self, name, breed):
    def __init__(self):
        #Animal.__init__(self, name)
        Animal.__init__(self)

class Canine(Animal):
    __attribute = "Canines belong to the Dog family"
    
    #def __init__(self, name, breed):
    def __init__(self):
        #Animal.__init__(self, name)
        Animal.__init__(self)

class Wolf(Canine):
    __attribute = "Wolves hunt in packs and have a leader"
    
    #def __init__(self, name, breed):
    def __init__(self):
        #Animal.__init__(self, name)
        Animal.__init__(self)

    @staticmethod
    def getAttribute():
        print(Tiger.__attribute)

class Tiger(Feline):
    __attribute = "Tigers can roar and are lethal predators"
    
    #def __init__(self, name, breed):
    def __init__(self):
        #Animal.__init__(self, name)
        Animal.__init__(self)

    @staticmethod
    def getAttribute():
        print(Tiger.__attribute)
    
class WildCat(Feline):
    __attribute = "Wild Cats can climb trees"
    
    #def __init__(self, name, breed):
    def __init__(self):
        #Animal.__init__(self, name)
        Animal.__init__(self)

    @staticmethod
    def getAttribute():
        print(WildCat.__attribute)    


#zoo=Zoo()
Zoo.add(Tiger())
Zoo.add(WildCat())
Zoo.add(Wolf())    
WildCat.getAttribute()
WildCat.getNumLegs()
#joe.getName()
#joe.run()
#print("Joe the ",joe.breed," has ",joe.getNumLegs()," legs")
#print("Joe's name is ",joe.getName1())
#print("Joe has",joe.getNumLegs(),"legs")

