animals = ['Tiger', 'WildCat', 'Wolf']

animal = list(filter(lambda a:a == 'Tiger', animals))

print(list(animal))

if len(animal) > 0:
	print('There is an animal in animal')
