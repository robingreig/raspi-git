# Calculate the area & perimeter of a rectangle

class Rectangle:
	'''Rectangle class will calculate area & perimeter'''
	
	def __init__(self, widthVal, heightVal):
		self.width = widthVal
		self.height = heightVal
	
	def getArea(self):
		return self.width * self.height
		
	def getPerimeter(self):
		return 2 * (self.width + self.height)
		
dim1 = float(input("Please enter the rectangle width: "))
dim2 = float(input("Please enter the rectangle height: "))

kitchen = Rectangle(dim1, dim2)

print("The kitchen area = ",kitchen.getArea())
print("The kitchen perimeter = ",kitchen.getPerimeter())
print("The kitchen area is: "+str(kitchen.getArea())+" And the kitchen perimeter is: "+str(kitchen.getPerimeter()))

