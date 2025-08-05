# DH OBSERVATORY CONTROLLER
from config.config import *
from dhoc.angles.getazimuth import get_azimuth
from utils.KermLib.KermLib import *
from dhoc.getdata.getplanet import *



KermLib.ascii_run()
print(f'Dominguez Hills Observatory Controller V{version}')
print('\n' * 2)



while True:
    selected_planet = get_planet()
    get_azimuth(selected_planet, dh_observatory_lat, dh_observatory_lon )


    user_input = input("Enter y if you'd like to find the Azimuth angle to a planet. Otherwise, enter n to close: ")
    user_input = user_input.strip().lower()
    if user_input == 'n':
        break