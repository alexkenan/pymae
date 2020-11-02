#!/usr/bin/env python3
"""
Create 2D and 3D static and animated visualizations for 2-body orbits

Produced for "Python for Mechanical and Aerospace Engineering" by Alex Kenan, ISBN 978-1-7360606-0-5 and 978-1-7360606-1-2.
Copyright © 2020 Alexander Kenan. Some Rights Reserved. This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. 
See http://creativecommons.org/licenses/by-nc-sa/4.0/ for more information.
"""
import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

# Create a Keplerian elliptical orbit with
# semi-major axis of 1.0 length units,
# a period of 1.0 time units, eccentricity of 0.5,
# longitude of ascending node of 0 degrees, an inclination
# of 30 deg, and a periapsis argument of 0 deg.
orbit = pyasl.KeplerEllipse(a=1.0, per=1.0, e=0.50, Omega=0.0,
                            i=30.0, w=0.0)

# Get a time axis
t = np.linspace(0, 4, 200)

# Calculate the orbit position at the given points
# in a Cartesian coordinate system.
pos = orbit.xyzPos(t)

# Plot x and y coordinates of the orbit with a few different options

# 2D, animated, and space
'''
plt.style.use('dark_background')
fig, ax = plt.subplots()
l = plt.plot(pos[::,1], pos[::,0], 'k-')


red_dot, = plt.plot(pos[0][1], pos[0][0], 'wo')

def animate(i):
    red_dot.set_data(pos[i][1], pos[i][0])
    return red_dot,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, 
                          frames=np.arange(0, len(t), 1), 
                          interval=40, blit=True, repeat=True)

plt.plot(0, 0, 'bo', markersize=9, label="Earth")
plt.tick_params(
    axis='both',  # changes apply to the x-axis
    which='both',  # both major and minor ticks are affected
    bottom=False,  # ticks along the bottom edge are off
    top=False,  # ticks along the top edge are off
    labelbottom=False,  # labels along the bottom edge are off
    left=False,
    labelleft=False)
plt.axis('off')
plt.title('Orbital Simulation')
plt.show()
'''

# 2D and space
'''
plt.style.use('dark_background')

# Plot the satellite orbit
plt.plot(pos[::, 1], pos[::, 0], 'w-', label="Satellite Trajectory")

# Point of periapsis
plt.plot(pos[0, 1], pos[0, 0], 'r*', label="Periapsis")

plt.plot(0, 0, 'bo', markersize=9, label="Earth")
plt.tick_params(
    axis='both',  # changes apply to the x-axis
    which='both',  # both major and minor ticks are affected
    bottom=False,  # ticks along the bottom edge are off
    top=False,  # ticks along the top edge are off
    labelbottom=False,  # labels along the bottom edge are off
    left=False,
    labelleft=False)
plt.axis('off')

plt.title('Orbital Simulation')
plt.show()
'''

# 2D, static, white background
'''
# Plot the Earth
plt.plot(0, 0, 'bo', markersize=9, label="Earth")

# Plot the satellite orbit
plt.plot(pos[::, 1], pos[::, 0], 'k-', label="Satellite Trajectory")

# Point of periapsis
plt.plot(pos[0, 1], pos[0, 0], 'r*', label="Periapsis")

plt.style.use('default')
plt.legend(loc="upper right")
plt.tick_params(
    axis='both',  # changes apply to the x-axis
    which='both',  # both major and minor ticks are affected
    bottom=False,  # ticks along the bottom edge are off
    top=False,  # ticks along the top edge are off
    labelbottom=False,  # labels along the bottom edge are off
    left=False,
    labelleft=False)
plt.title('Orbital Simulation')
plt.axis('off')
plt.show()
'''

# 2D, animated, white background
'''
fig, ax = plt.subplots()
plt.plot(pos[::, 1], pos[::, 0], 'c-')

red_dot, = plt.plot(pos[0][1], pos[0][0], 'ro')


def animate(i):
    red_dot.set_data(pos[i][1], pos[i][0])
    return red_dot,


# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, 
                          frames=np.arange(0, len(t), 1), 
                          interval=40, blit=True, repeat=True)

plt.plot(0, 0, 'bo', markersize=9, label="Earth")
plt.tick_params(
    axis='both',  # changes apply to the x-axis
    which='both',  # both major and minor ticks are affected
    bottom=False,  # ticks along the bottom edge are off
    top=False,  # ticks along the top edge are off
    labelbottom=False,  # labels along the bottom edge are off
    left=False,
    labelleft=False)
plt.style.use('default')
plt.title('Orbital Simulation')
plt.axis('off')
plt.show()
'''

# 3D, dark background
'''
plt.style.use('dark_background')
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D([0], [0], [0], 'bo', markersize=9, label="Earth")

# Plot the satellite orbit
ax.plot3D(pos[::, 1], pos[::, 0], pos[::, 2], 'w-',
          label="Satellite Trajectory")

# Point of periapsis
#ax.plot3D([pos[0, 1]], [pos[0, 0]], [pos[0, 2]], 'r*', label="Periapsis")

plt.legend(loc="lower right")

# Hide grid lines
ax.grid(False)

# Hide axes ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.title('Orbital Simulation')
plt.axis('off')
plt.show()
'''

# 3D, white background
'''
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D([0], [0], [0], 'bo', markersize=9, label="Earth")

# Plot the satellite orbit
ax.plot3D(pos[::, 1], pos[::, 0], pos[::, 2], 'k-',
          label="Satellite Trajectory")

# Point of periapsis
ax.plot3D([pos[0, 1]], [pos[0, 0]], [pos[0, 2]], 'r*', 
          label="Periapsis")

plt.legend(loc="lower right")
plt.style.use('default')
# Hide grid lines
ax.grid(False)

# Hide axes ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.title('Orbital Simulation')
plt.show()
'''

# 3D, white background, animated
#'''
fig = plt.figure()
ax = p3.Axes3D(fig)

red_dot, = ax.plot(pos[::, 1], pos[::, 0], pos[::, 2], 'ro', 
                   label="Satellite")


def animate(i, pos, red_dot):
    red_dot.set_data([pos[i][1], pos[i][0]])
    red_dot.set_3d_properties(pos[i][2])
    return red_dot,


# create animation using the animate() function
ani = animation.FuncAnimation(fig, animate, 200, fargs=(pos, red_dot),
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

