# Calculate the area & perimeter of a rectangle

class Rectangle:
	'''Rectangle class will calculate area & perimeter'''
	count = 0 # initialize count variable and start at 0
	
	def __init__(self, widthVal, heightVal):
		self.width = widthVal
		self.height = heightVal
		self.count += 1
		Rectangle.count += 1

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
print("Rectangle Count = "+str(Rectangle.count))
print("Kitchen Count = "+str(kitchen.count))

dim3 = float(input("Please enter the bedroom width: "))
dim4 = float(input("Please enter the bedroom height: "))

bedroom = Rectangle(dim3, dim4)

print("The bedroom area = ",bedroom.getArea())
print("The bedroom perimeter = ",bedroom.getPerimeter())
print("The bedroom area is: "+str(bedroom.getArea())+" And the kitchen perimeter is: "+str(bedroom.getPerimeter()))
print("Rectangle Count = "+str(Rectangle.count))
print("Kitchen Count = "+str(kitchen.count))
print("Bedroom Count = "+str(bedroom.count))

dim5 = float(input("Please enter the upstairs width: "))
dim5 = float(input("Please enter the upstairs height: "))

upstairs = Rectangle(dim3, dim4)

print("The upstairs area = ",bedroom.getArea())
print("The upstairs perimeter = ",bedroom.getPerimeter())
print("The upstairs area is: "+str(bedroom.getArea())+" And the kitchen perimeter is: "+str(bedroom.getPerimeter()))
print("Rectangle Count = "+str(Rectangle.count))
print("Kitchen Count = "+str(kitchen.count))
print("Bedroom Count = "+str(bedroom.count))
print("Upstairs Count = "+str(upstairs.count))
