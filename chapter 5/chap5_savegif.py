# !/usr/bin/env python3
"""
Graph 2D and 3D elliptical orbits with PyAstronomy and matplotlib, and
animate the 2D orbit
"""
import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
writer = PillowWriter(fps=30)

orbit = pyasl.KeplerEllipse(a=1.0, per=1.0, e=0.50, Omega=0.0,
                            i=30.0, w=0.0)

t = np.linspace(0, 4, 200)

pos = orbit.xyzPos(t)

plt.style.use('dark_background')
fig, ax = plt.subplots()
l = plt.plot(pos[::,1], pos[::,0], 'k-')

red_dot, = plt.plot(pos[0][1], pos[0][0], 'wo')

def animate(i):
    red_dot.set_data(pos[i][1], pos[i][0])
    return red_dot,


# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate,
                    frames=np.arange(0, len(t), 1), interval=40,
                    blit=True, repeat=True)

plt.plot(0, 0, 'bo', markersize=9, label="Earth")
plt.tick_params(
    axis='both',
    which='both',
    bottom=False,
    top=False,
    labelbottom=False,
    left=False,
    labelleft=False)

plt.legend(loc="upper right")
plt.title('Orbital Simulation')
myAnimation.save('/Users/Alex/Desktop/myAnimation.gif',
                 writer=writer)
