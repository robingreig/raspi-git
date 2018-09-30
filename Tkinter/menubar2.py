from Tkinter import *

class App:
	def __init__(self, master):
		frame = Frame(master, width=400, height=10)
		frame.pack()

		menubar= Menu(root)
		menubar.add_command(label="Hello", command=self.say_hi)
		menubar.add_command(label="Quit", command=root.quit)
		root.config(menu=menubar)

		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Open", command=self.say_open)
		filemenu.add_command(label="Close", command=self.say_close)
		filemenu.add_separator()
		filemenu.add_command(label="Left", command=self.say_left)
		filemenu.add_command(label="Right", command=self.say_right)

		menubar.add_cascade(label="File", menu=filemenu)

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

		self.button1 = Button(
#			frame, text="QUIT", fg="red", command=frame.quit
			text="QUIT", fg="red", command=frame.quit
			)
#		self.button1.pack(side=LEFT)
		self.button1.pack()

		separator = Frame(height=2, bd=1, relief=SUNKEN)
		separator.pack(fill=X, padx=5, pady=5)

		self.var1 = IntVar()
		self.button3 = Checkbutton(
			text="Color Image", variable=self.var1,
			command=self.cb
			)
		self.button3.pack()

		separator = Frame(height=2, bd=1, relief=SUNKEN)
		separator.pack(fill=X, padx=5, pady=5)

		group = LabelFrame(
			text="Group", padx=5, pady=5
			)
		group.pack(padx=10, pady=10)

		MODES = [
			("Button1", "1"),
			("Button2", "2"),
			("Button3", "Robin"),
			("Button4", "Greig"),
		]
		
		self.var2 = StringVar()
		self.var2.set("1")

		for text, mode in MODES:
			b = Radiobutton(
				text=text, variable=self.var2, value=mode,
				command=self.rb1, pady=5
			)
			b.pack(anchor=W, padx=150)

		separator = Frame(height=2, bd=1, relief=SUNKEN)
		separator.pack(fill=X, padx=5, pady=5)

		group = LabelFrame(
			text="Group", padx=5, pady=5
			)
		group.pack(padx=10, pady=10)

		MODES = [
			("Button1", "1"),
			("Button2", "2"),
			("Button3", "Robin"),
			("Button4", "Greig"),
		]
		
		self.var3 = StringVar()
		self.var3.set("1")

		for text, mode in MODES:
			b = Radiobutton(
				text=text, variable=self.var3, value=mode,
				indicatoron=0, command=self.rb2, pady=10
			)
			b.pack(anchor=W, padx=150)

		separator = Frame(height=2, bd=1, relief=SUNKEN)
		separator.pack(fill=X, padx=5, pady=5)

	def say_hi(self):
		print"hi there everyone!"

	def say_open(self):
		print"Open a file"

	def say_close(self):
		print"Close a file"

	def say_left(self):
		print"Go left"

	def say_right(self):
		print"Go right"

	def cb(self):
		print "Checkbutton variable is: ", self.var1.get()

	def rb1(self):
		print "Radiobutton variable is: ", self.var2.get()

	def rb2(self):
		print "Radiobutton (IndicatorOn) variable is: ", self.var3.get()

root = Tk()

app = App(root)

root.mainloop()

root.destroy()


