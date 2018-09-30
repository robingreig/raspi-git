from Tkinter import *

class App:
	def __init__(self, master):
		frame = Frame(master, width=500, height=400)
		frame.pack()

		separator = Frame(height=2, bd=1, relief=SUNKEN)
		separator.pack(fill=X, padx=5, pady=5)

		self.button2 = Button(
#			frame, text="HELLO", command=self.say_hi
			text="HELLO", command=self.say_hi
			)

#		self.button2.pack(side=RIGHT)
		self.button2.pack()

		separator = Frame(height=2, bd=1, relief=SUNKEN)
		separator.pack(fill=X, padx=5, pady=5)


		self.label1 = Label(text="one").pack()

		separator = Frame(height=2, bd=1, relief=SUNKEN)
		separator.pack(fill=X, padx=5, pady=5)

		self.label2 = Label(text="two").pack()

		separator = Frame(height=2, bd=1, relief=SUNKEN)
		separator.pack(fill=X, padx=5, pady=5)

		self.button1 = Button(
#			frame, text="QUIT", fg="red", command=frame.quit
			text="QUIT", fg="red", command=frame.quit
			)
#		self.button1.pack(side=LEFT)
		self.button1.pack()

		separator = Frame(height=2, bd=1, relief=SUNKEN)
		separator.pack(fill=X, padx=5, pady=5)


	def say_hi(self):
		print"hi there everyone!"

root = Tk()

app = App(root)

root.mainloop()

root.destroy()


