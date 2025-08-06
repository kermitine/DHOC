# find azimuth angle from CSUDH observatory to a given celestial object 

# latitude and longitude of observatory: 33.863907,-118.255190

# cross reference with planetscalc azimuth calculator


from skyfield.api import load
from skyfield.toposlib import Topos
ts = load.timescale()


def get_azimuth(selected_planet, lat, lon):
    planets = load('de441.bsp')  # Ephemeris file
    earth = planets['earth']
    target = planets[selected_planet]  # or any other planet

    location = earth + Topos(lat, lon)


    t = ts.now()
    astrometric = location.at(t).observe(target)
    alt, az, distance = astrometric.apparent().altaz()
    return az.degrees