def circle(radius):
    print("Area of Circle",3.14*radius*radius)

def rectangle(length,breadth):
    print("Area of Rectangle:",length*breadth)
    
def square(side):
    print("Area:",side*side)

while True:
    print("Menu Driven Program")
    print("1.Area of Circle")
    print("2.Area of Rectangle")
    print("3.Area of Square")    
    print("4.Exit")
    choice=int(input("Enter your choice:"))


    if choice==1:
        radius=int(input("Enter radius of Circle:"))
        circle(radius)


    elif choice==2:
        length=int(input("Enter length of Rectangle:"))
        breadth=int(input("Enter breadth of Rectangle:"))
        rectangle(length,breadth)
    
    elif choice==3:
        side=int(input("Enter side of Square:"))
        square(side)


    elif choice==4:
        break
    else:
        print("Wrong Choice")
