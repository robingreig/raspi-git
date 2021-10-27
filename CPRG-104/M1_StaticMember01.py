# -*- coding: utf-8 -*-
"""
Created on 2021/10/24 09:46:14

"""
class Person:
	'''This is a person class'''
	profession = "student" # Assign static attribute

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print(self.name)
		print(self.age)
	
	def greeting(self):
		print("Welcome to CPRG 104 "+self.name)

	def getAge(self):
		return self.age

	def setName(self,nameValue):
		self.name = nameValue
	
	def getInfo(self):
		print("Name: "+self.name+", Age: "+str(self.age))
	
	@staticmethod
	def getProfession():
		return Person.profession
	
print(Person.greeting)
print(Person.__doc__)

Robin = Person("Fred", 22)

print(Robin.greeting())
print("Robin object's Age: "+str(Robin.age))
print("Robin object's Name: "+Robin.name)
print(Robin.getAge())
print(Robin.name)
print(Robin.setName("Greig"))
print(Robin.name)
print(Robin.getInfo())
print(Person.profession) # Access static attribute
print(Person.getProfession())
