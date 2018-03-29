import matplotlib
# Run headless
matplotlib.use('agg')

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

plt.plot([1,2,3,4])
plt.ylabel('some numbers')

fig.savefig('/home/robin/MatPlotLib11.png')

# evenly sampled time at 200ms intervals
#t = np.arange(0., 5., 0.2)

#fig = plt.figure()
#red dashes, blue squares, & green triangles
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#fig.savefig('/home/robin/MatPlotLib.png')
#plt.show()

