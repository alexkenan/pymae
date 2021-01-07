# Correction

Turns out, I was right to be skeptical of 1 billion psf as the maximum dynamic pressure! I mis-interpreted the NASA atmospheric model and treated pressure as density. 
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

        rho = p/(1718*(temp+459.7))
        return rho
