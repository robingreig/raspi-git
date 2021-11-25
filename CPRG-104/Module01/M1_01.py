class Person:
    '''This is a person class'''
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
	
print(Person.greeting)
print(Person.__doc__)

Robin = Person("Fred", 22)

print(Robin.greeting())
print(Robin.age)
print(Robin.name)
print(Robin.getAge())
print(Robin.name)
print(Robin.setName("Greig"))
print(Robin.name)
