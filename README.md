# Python for Mechanical and Aerospace Engineering
by Alex Kenan


## What is this this?

This is the GitHub repository for the book *Python for Mechanical and Aerospace Engineering* by Alex Kenan. This repository contains completed programs for the nine chapters as well as the entire 595 page syllabus and course materials for an internal NSA "Introduction to Python" class that was made available by a Freedom of Information Act request.

**chapter 1.5**:  FizzBuzz with Python to demonstrate a basic Python program  
**chapter 2**:	Graphing thrust required and thrust available for an Airbus A321 at three different altitudes with **Matplotlib**  
**chapter 3**:	Graphing dynamic pressure as a function of time for a rocket launch with **Matplotlib**    
**chapter 4**:	Getting and plotting airfoil coordinates with **Requests** and **Matplotlib**  
**chapter 5**:	Modeling a satellite’s orbit around Earth with **PyAstronomy** and **Matplotlib**  
**chapter 6**:	Creating a GUI to convert units with **Tkinter** and **Pint**  
**chapter 7**:	Introduction to web scraping (**Requests** and **BeautifulSoup4**) and exporting data to Excel (**Openpyxl**)  
**chapter 8**:	Modeling camera shutter effect on an aircraft’s propeller with **Tkinter** and **Numpy**    
**chapter 9**:	Making pdf reports of Python code with **Pweave**  


[Learn more about Python for Mechanical and Aerospace Engineering here](https://www.alexkenan.com/pymae/)


<center><a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a></center><br />
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Correction

Turns out, I was right to be skeptical of 1 billion psf as the maximum dynamic pressure in Chapter 3! I mis-interpreted the NASA atmospheric model and treated pressure as density. 
This corrected density function should give you the original Max Q psf average acceleration of 1,395 psf:

    def density_corrected(height: float) -> float:
        """
        Returns the air density in slug/ft^3 based on altitude
        Equations from https://www.grc.nasa.gov/www/k-12/rocket/atmos.html
        :param height: Altitude in feet
        :return: Density in slugs/ft^3
        """
        if height < 36152.0:
            temp = 59 - 0.00356 * height
            p = 2116 * ((temp + 459.7)/518.6)**5.256
        elif 36152 <= height < 82345:
            temp = -70
            p = 473.1*np.exp(1.73 - 0.000048*height)
        else:
            temp = -205.05 + 0.00164 * height
            p = 51.97*((temp + 459.7)/389.98)**-11.388

        rho = p/(1718*(temp + 459.7))
        return rho
