import os, time

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
     print('Handle option \'Option 1\'')
     input("Press any key to continue")
     
def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')

if __name__=='__main__':
    while(a == 1):
        screen_clear()
        print_menu()
        option = ''
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
            time.sleep(2)
