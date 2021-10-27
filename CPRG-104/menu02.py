menu = {}
menu['1']="Add Student." 
menu['2']="Delete Student."
menu['3']="Find Student"
menu['4']="Exit"
while True: 
  options=menu.keys()
  options.sort()
  for entry in options: 
    print entry, menu[entry]

    selection=raw_input("Please Select:") 
    if selection =='1': 
      print "add" 
    elif selection == '2': 
      print "delete"
    elif selection == '3':
      print "find" 
    elif selection == '4': 
      break
    else: 
      print "Unknown Option Selected!" 
