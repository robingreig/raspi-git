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
		
	def setWidth(self, newWidth):
		self.width = newWidth
		
dim1 = float(input("Please enter the kitchen width: "))
dim2 = float(input("Please enter the kitchen height: "))

kitchen = Rectangle(dim1, dim2)

print("The kitchen area = ",kitchen.getArea())
print("The kitchen perimeter = ",kitchen.getPerimeter())
print("The kitchen area is: "+str(kitchen.getArea())+" And the kitchen perimeter is: "+str(kitchen.getPerimeter()))

dim3 = float(input("Please enter the bedroom width: "))
dim4 = float(input("Please enter the bedroom height: "))

bedroom = Rectangle(dim3, dim4)

print("The bedroom area = ",bedroom.getArea())
print("The bedroom perimeter = ",bedroom.getPerimeter())
print("The bedroom area is: "+str(bedroom.getArea())+" And the kitchen perimeter is: "+str(bedroom.getPerimeter()))
