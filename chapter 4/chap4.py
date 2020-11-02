# !/usr/bin/env python3
"""
Graph 2D airfoils using University of Indiana at Urbana-Champaign (UIUC) website

Produced for "Python for Mechanical and Aerospace Engineering" by Alex Kenan, ISBN 978-1-7360606-0-5 and 978-1-7360606-1-2.
Copyright © 2020 Alexander Kenan. Some Rights Reserved. This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. 
See http://creativecommons.org/licenses/by-nc-sa/4.0/ for more information.
"""
import requests
import matplotlib.pyplot as plt


def get_airfoil_coords(airfoil: str) -> tuple:
    """
    Get airfoil coords from UIUC website
    https://m-selig.ae.illinois.edu/ads/coord/__.dat
    :param airfoil: str of airfoil types
    :return: tuple of ([x coords], [y coords], plot_title)
    """
    url = 'https://m-selig.ae.illinois.edu/ads/coord/{}.dat'.format(airfoil.lower())
    headers = {'user-agent':
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0'}
    response_text = requests.get(url, headers=headers).text

    if 'Not Found' in response_text:
        raise NameError('{} not found in UIUC database'.format(airfoil))

    all_text = response_text.split('\n')
    x_coordinates, y_coordinates = [], []
    plot_title = ''

    for index, line in enumerate(all_text):
        if index == 0:
            plot_title = line.strip()
        else:
            try:
                line = line.strip()
                x, y = line.split(' ' * line.count(' ')) # line changed
                x = float(x.strip())
                y = float(y.strip())
                if x <= 1.0 and y <= 1.0: # line changed
                    x_coordinates.append(x)
                    y_coordinates.append(y)
            except ValueError:
                continue



    return x_coordinates, y_coordinates, plot_title


def plot_airfoil(x_coordinates: list, y_coordinates: list, plot_title: str) -> None:
    """
    Plot the airfoil coordinates given the list of coordinates

    :param x_coordinates: list of airfoil's x coordinates
    :param y_coordinates: list of airfoil's y coordinates
    :param plot_title: str to title as the plot's title
    :return: None
    """
    plt.style.use('default')
    plt.plot(x_coordinates, y_coordinates, 'k-')

    plt.title('{} airfoil'.format(plot_title))
    plt.xlim(-0.50, 1.25)
    plt.ylim(-1, 1)
    plt.show()

air_foil = 'mh70'
try:
    x_values, y_values, title = get_airfoil_coords(air_foil)

    plot_airfoil(x_values, y_values, title)
except NameError:
    print('{} not in UIUC database, try again!'.format(air_foil))

