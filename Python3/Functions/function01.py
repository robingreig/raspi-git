#!/usr/bin/python3

v = 5

def printme(v):
    y1 = v
    y2 = v + v
    y3 = v + v +v
    return {'a':y1, 'b':y2, 'c':y3}
# Original method of using a dictionary
#    d = dict();
#    d[1] = y1
#    d[2] = y2
#    d[3] = y3
#    return d
# print ("Y1 within d is: ",d[1])

d = printme(v)

print("All of d is: ",d)
print("Y1 within d is: ",d['a'])
print("Y2 within d is: ",d['b'])
print("Y3 within d is: ",d['c'])

