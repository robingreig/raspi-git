import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('/home/robin/raspi-git/Python/MatPlotLib/exercise31.txt','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))

plt.plot(x,y, label='loaded from file!')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('First CSV graph!!\nWith a double line')
plt.legend()
plt.show()
