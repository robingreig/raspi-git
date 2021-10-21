# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 08:59:30 2021

"""


class student:

    __profession = "student"  #private static attribute
    
    def __init__(self, name, age, email):
         self.name = name
         self.age = age
         self.email = email
    
    def getEmail(self):
        return self.email
    
    def updateAge(self, newAge):
        self.age = newAge
    
    def study(self):
        print(self.name + " is studying")

    def getInfo(self):
        print("Name: " + self.name + " Age: " 
              + str(self.age) + " Email: " + self.email);
  
    @staticmethod   #static method
    def getProfession():
        return student.__profession


print(student.getProfession()) #invoke static method
#print(student.__profession)  #access private 
                            #static attribute
                            #lead to error

alex = student("Alex",25,"alex@gmail.com")
print(alex.getEmail())
alex.study()
alex.getInfo()
alex.updateAge(26)
alex.getInfo()

