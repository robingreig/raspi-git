# -*- coding: utf-8 -*-
"""
Robin Greig
robin.01.01.py
2021.10.21
"""

class student:
	__profession = "student" #private static attribute
	
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
			print("Name: " + self.name + "Age: " + self.age
				+ "Email: " + self.email)
				
		@staticmethod
		def getProfession():
			return student.__profession
			
print(student.getProfession()) # invoke static method

robin = student("Robin", "61", "robin.greig@sait.ca")
print("Robin's email: "+ robin.getEmail
