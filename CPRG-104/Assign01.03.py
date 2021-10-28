import os, time

class Animal:
	''' This is the grandparent class for all of the Animals'''
	__hands = 2 # Assign a private static attribute
	zooCount = 0 # Number of animals or birds in the zoo
	animalCount = 0 # number of animals in the zoo

	def __init__(self, typeAnimal):
		self.breed = typeAnimal
		print("self.breed = ",self.breed)
		Animal.zooCount += 1 # increment the number of anmimals/birds in the zoo
		Animal.animalCount += 1 # increment the number of animals
		print("zooCount = "+str(self.zooCount))
		print("animalCount = "+str(self.animalCount))
#		time.sleep(2)

	def getZooCount(self):
		print("Zoo count from Animal Class: "+str(self.zooCount))
#		time.sleep(5)
		#return Animal.zooCount

	def getAnimalCount(self):
		print("Animal Count from Animal Class: "+str(self.animalCount))
		return self.animalCount
		
	def getAnimalInfo(self):
		print("The animal is a: "+str(self.breed))
		
	def getAnimalInfo2(self):
		return self.breed

class Bird:
	''' This is the grandparent class for all of the Birds'''
	__hands = 2 # Assign a private static attribute
	birdCount = 0 # number of birds in the zoo

	def __init__(self, typeBird):
		self.genus = typeBird
		print("self.genus = ",self.genus)
		Bird.birdCount += 1 # increment the number of birds
		print("birdCount = "+str(self.birdCount))
#		time.sleep(2)

	def getBirdCount(self):
		print("Bird Count from Bird Class: "+str(self.birdCount))
		
	def getBirdInfo(self):
		print("The bird is a: "+str(self.genus))

def addAnimal():
	if Animal.animalCount == 2:
		print(" You have 2 animals in your zoo and cannot add more")
		time.sleep(2)
		return
	typeAnimal = raw_input("What is the breed of your animal? " ).lower()
	# .lower on previous command sets the case of the input to all lower
	if Animal.animalCount == 1:
		breed2 = Animal(typeAnimal)
		print("this is the second animal and it is a: "+breed2.breed)
		breed2.getZooCount()
		breed2.getAnimalInfo()
		print("And you cannot add additional animals to your zoo!")
		time.sleep(3)
	if Animal.animalCount == 0:
		breed1 = Animal(typeAnimal)
		print("This is the first animal and it is a: "+breed1.breed)
		animalNum = "second"
		print("Printing breed1.getZooCount()")
		breed1.getZooCount()
		print("Printing breed1.getInfo()")
		breed1.getAnimalInfo()
		time.sleep(5)

def addBird():
	if Bird.birdCount == 1:
		print(" You have 1 bird in your zoo and cannot add more")
		time.sleep(2)
		return
	typeBird = raw_input("What is the breed of your bird? " ).lower()
	# .lower on previous command sets the case of the input to all lower
	if Bird.birdCount == 0:
		breed3 = Bird(typeBird)
		print("this is the first bird and it is a: "+breed3.genus)
		breed3.getBirdCount()
		breed3.getBirdInfo()
		print("And you cannot add additional birds to your zoo!")
		time.sleep(3)

def showZoo():
		print("this is the showZoo function")
#		time.sleep(2)
		try:
			print("Trying breed1.getAnimalInfo()")
			#breed1.getZooCount()

		except:
			print("There are no animals in your zoo")


def screen_clear(): # The function to clear the screen between inputs
   # Windows has a different clear screen command than linux & iOS
   # Windows uses 'cls" and linux / iOS uses 'clear'
   # So for my raspberry pi or iOS, my system name = 'posix'
	if os.name == 'posix':
		_ = os.system('clear')
	else:
      # for windows platfrom
		_ = os.system('cls')

a = 1 # value for variable in while loop
      # and my way to exit from the try/except loop

menu_options = {
    1: 'Add an animal to your zoo',
    2: 'Add a bird to your zoo',
    3: 'View all of the animals in your Zoo',
    4: 'Exit',
}

def print_menu():
	for key in menu_options.keys():
		print (key, menu_options[key] )

def option1():
	addAnimal() # Execute the addAminal Function

def option2():
	addBird() # Execute the addBird Function

def option3():
	#showZoo() # Execute the showZoo function
	#breed1.getAnimalInfo()
	#breed1.getAnimalInfo2()
	print("breed1: ",breed1.getAnimalInfo2())
			
while(a == 1):
#	screen_clear()
	print_menu()
	option = 0
	try:
		option = int(input('Enter your choice: '))
		if option == 1:
			option1()
		elif option == 2:
			option2()
		elif option == 3:
			option3()
		elif option == 4:
			print('Thanks for visting our Zoo!')
			a = 0   
	except:
		print('Wrong input. Please enter a number between 1 and 4')

