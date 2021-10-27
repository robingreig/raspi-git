# -*- coding: utf-8 -*-
"""
Created on 2021/10/24 09:46:14

"""
animalNum = "first"

class Zoo:
	'''This is a zoo class'''
	__hands = 2 # Assign a protected static attribute
	__wings = 2 # Assign a protected static attribute
	count = 0
	animalCount = 0
	birdCount = 0

	def __init__(self, typeAnimal):
		self.breed = typeAnimal
		print(self.breed)
		Zoo.count += 1
	
	def getZooCount(self):
		return Zoo.count


while Zoo.count < 5:
	print("Zoo Count at the start of the while loop: "+str(Zoo.count))
	typeAnimal = raw_input("What is the "+str(animalNum)+" animal or bird type?: ").lower()
	print("Input received = "+typeAnimal)
	if animalNum == 'third':
		breed3 = Zoo(typeAnimal)
		print("This is the third animal and it is a: "+breed3.breed)
		print("Zoo count = "+str(Zoo.count))
	if animalNum == 'second':
		breed2 = Zoo(typeAnimal)
		animalNum = 'third'
		print("This is the second animal and it is a: "+breed2.breed)
		print("Zoo count = "+str(Zoo.count))
	if animalNum == 'first':
		breed1 = Zoo(typeAnimal)
		animalNum = 'second'
		print("This is the first animal and it is a: "+breed1.breed)
		print("Zoo Count = "+str(Zoo.count))
	if int(Zoo.count) == 3:
		print("Your Zoo is full")
		break


'''	elseif int(Zoo.count) == 2:
		breed2 = Zoo(typeAnimal)
		animalNum = "third"
	else:
		breed3 = Zoo(typeAnimal) '''

	


if breed1.breed == "tiger":
	print("Yikes it's a TIGER!!!")
	
'''	def greeting(self):
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
	
	@staticmethod
	def getProfession1():
		return Person._profession1

	@staticmethod
	def getProfession2():
		return Person.__profession2

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
print(Person.profession) # Access public static attribute
print(Person.getProfession())
#print(Person.profession1) # Access protected static attribute
print(Person.getProfession1())
#print(Person.profession2) # Access private static attribute
print(Person.getProfession2())
'''
