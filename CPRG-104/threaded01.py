from threading import Thread
def threaded_function(arg):
	for i in range(arg):
		print("Robin Greig")
	if __name__ == "__main__":
		thread = Thread(target = threaded_function, args = (3, ))
		thread.start()
		thread.join()
		print("Thread exiting")
		

	
