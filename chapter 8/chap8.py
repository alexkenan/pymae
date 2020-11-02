#!/usr/bin/env python3
"""
Graphically show camera shutter effect

Produced for "Python for Mechanical and Aerospace Engineering" by Alex Kenan, ISBN 978-1-7360606-0-5 and 978-1-7360606-1-2.
Copyright © 2020 Alexander Kenan. Some Rights Reserved. This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. 
See http://creativecommons.org/licenses/by-nc-sa/4.0/ for more information.
"""

import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

root = tk.Tk()
stage = tk.Label(root)
stage.pack()
height = 300
num_propeller_blades = 4
x, y = np.ogrid[-height/2: height/2, -height/2: height/2]
plane = x - 1j * y
bentprop = np.zeros_like(plane, dtype=np.bool)

for frame in range(height):
    backgnd = np.zeros_like(plane, dtype=np.uint8)
    propeller = np.zeros_like(plane, dtype=np.bool)
    angle = 2 * np.pi * (frame / height)
    for blade in range(num_propeller_blades):
        phase = np.exp(1j * (angle + blade * np.pi / (num_propeller_blades / 2)))
        ellipse = abs(plane - 0.48 * height * phase) + abs(plane)
        propeller |= ellipse < 0.49 * height

    bentprop[frame] = propeller[frame]
    shutter_pan = [f for f in range(frame, min(frame + 3, height - 3))]
    colors = ("white", "black", "red", "blue")
    rgbcolors = np.array(list(map(root.winfo_rgb, colors))) / 256
    composite = np.maximum.reduce((backgnd, propeller * 1, bentprop * 2))
    composite[shutter_pan] = 3
    rgb = rgbcolors.astype(np.uint8)[composite]
    image = ImageTk.PhotoImage(Image.fromarray(rgb, mode="RGB"))
    stage.config(image=image)
    root.update()

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)
root.title('{} blade propeller camera effect'.format(num_propeller_blades))
root.mainloop()
