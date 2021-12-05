thisdict = {
	"brand": "GMC",
	"model": "Equinox",
	"year": "2011"
}
print(thisdict)
print(len(thisdict))
w = thisdict.items()
x = thisdict.keys()
y = thisdict.values()
print('list of items',w)
print('list of keys: ',x)
print('list of values: ',y)
z = thisdict.get('year')
print('just the year: ',z)
thisdict['color'] = 'white'
print(x)
print(y)
print('for loop:\n')
for x in thisdict:
	print(thisdict[x])
