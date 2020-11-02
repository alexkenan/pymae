# !/usr/bin/env python3
"""
Create a visualization for the Molniya satellite orbit. 

Produced for "Python for Mechanical and Aerospace Engineering" by Alex Kenan, ISBN 978-1-7360606-0-5 and 978-1-7360606-1-2.
Copyright © 2020 Alexander Kenan. Some Rights Reserved. This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. 
See http://creativecommons.org/licenses/by-nc-sa/4.0/ for more information.
"""

import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

# 2D Molniya
'''
# Create the Molniya orbit
orbit = pyasl.KeplerEllipse(a=26600, per=0.55, e=0.737, Omega=0.0, i=63.4, w=270)

# Get a time axis
t = np.linspace(0, 4, 200)

# Calculate the orbit position at the given points
# in a Cartesian coordinate system.
pos = orbit.xyzPos(t)

# get the plot and axes ready
fig = plt.figure()
ax = plt.axes(projection='3d')

# plot Earth
ax.plot3D([0], [0], [0], 'bo', markersize=9, label="Earth")

# Plot the satellite orbit
ax.plot3D(pos[::, 1], pos[::, 0], pos[::, 2], 'k-', label="Satellite Trajectory")

# plot the legend
plt.legend(loc="lower right")

# Hide grid lines
ax.grid(False)

# Hide axes ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

plt.title('Orbital Simulation')
plt.show()
'''

# 3D Molniya
#'''
orbit = pyasl.KeplerEllipse(a=26600, per=0.55, e=0.737, Omega=0.0,
                            i=63.4, w=270)

# Get a time axis
t = np.linspace(0, 4, 1000)

# Calculate the orbit position at the given points
# in a Cartesian coordinate system.
pos = orbit.xyzPos(t)

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

red_dot, = ax.plot(pos[::, 1], pos[::, 0], pos[::, 2], 'ro', 
                   label="Satellite")


def animate(i, pos, red_dot):
    red_dot.set_data([pos[i][1], pos[i][0]])
    red_dot.set_3d_properties(pos[i][2])
    return red_dot,


# create animation using the animate() function
ani = animation.FuncAnimation(fig, animate, len(t), fargs=(pos, red_dot),
                              interval=100, blit=False)

ax.plot([0], [0], [0], 'bo', markersize=9, label="Earth")
ax.plot(pos[::, 1], pos[::, 0], pos[::, 2], 'k-',
        label="Satellite Trajectory")

# Hide grid lines
ax.grid(False)

# Hide axes ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.style.use('default')
plt.legend()
plt.show()
#'''
