"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the DHOC project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

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