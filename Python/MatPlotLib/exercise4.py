import matplotlib
# Run headless
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

fig = plt.figure()
#red dashes, blue squares, & green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
fig.savefig('/home/robin/MatPlotLib.png')
#plt.show()
