import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt ('/home/robin/raspi-git/Python/MatPlotLib/exercise31.txt', delimiter=',', unpack = True)

plt.plot(x,y, label='loaded from file!')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('First Numpy graph!!\nWith a double line')
plt.legend()
plt.show()
