import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

plt.figure(figsize = (5,7))

plt.subplot()

fig = plt.figure(figsize=(5,7))
spec = fig.add_gridspec(ncols=1, nrows=2, height_ratios=[5,2])

ax1 = fig.add_subplot(spec[0,0])
plt.title('infection simulation')

ax2 = fig.add_subplot(spec[1,0])
ax2.set_title('number of infected')
#ax2.set_xlim(0, simulation_steps)

ax1.clear()
ax2.clear()


plt.show()