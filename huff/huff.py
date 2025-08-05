# find azimuth angle from CSUDH observatory to a given celestial object 

# latitude and longitude of observatory: 33.863907,-118.255190

from skyfield.api import load
from skyfield.toposlib import Topos
import time

dh_observatory_lat = 33.863907
dh_observatory_lon = -118.255190
target_planet = 'mars'


# Load planetary data
planets = load('de421.bsp')  # Ephemeris file
earth = planets['earth']
mars = planets['mars']  # or any other planet


location = earth + Topos(dh_observatory_lat, dh_observatory_lon)


ts = load.timescale()


while True:
    t = ts.now()
    astrometric = location.at(t).observe(mars)
    alt, az, distance = astrometric.apparent().altaz()
    print(f'Compass Azimuth from DH Observatory to Mars: {az.degrees}')
    time.sleep(0.1)