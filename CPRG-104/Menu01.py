def my_add_fn():
   print "SUM:%s"%sum(map(int,raw_input("Enter 2 numbers seperated by a space").split()))

def my_quit_fn():
   raise SystemExit

def invalid():
   print "INVALID CHOICE!"

menu = {"1":("Sum",my_add_fn),
        "2":("Quit",my_quit_fn)
       }
for key in sorted(menu.keys()):
     print key+":" + menu[key][0]

ans = raw_input("Make A Choice")
menu.get(ans,[None,invalid])[1]()
