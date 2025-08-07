# Copyright (C) 2025 Ayrik Nabirahni
# This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see https://www.gnu.org/licenses.


# find azimuth angle from CSUDH observatory to a given celestial object 
# latitude and longitude of observatory: 33.863907,-118.255190
# cross reference with planetscalc azimuth calculator


from skyfield.api import load
from skyfield.toposlib import Topos
ts = load.timescale()


def get_azimuth(selected_planet, lat, lon):
    global ts 
    planets = load('de441.bsp')  # Ephemeris file
    earth = planets['earth']

    try:
        target = planets[selected_planet]  # or any other planet
    except ValueError:
        return 'noplanet'

    location = earth + Topos(lat, lon)


    t = ts.now()
    astrometric = location.at(t).observe(target)
    alt, az, distance = astrometric.apparent().altaz()
    return az.degrees