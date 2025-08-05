# DH OBSERVATORY CONTROLLER
from config.config import *
from dhoc.angles.getazimuth import get_azimuth
from utils.KermLib.KermLib import *
from dhoc.getdata.getplanet import *
import time




KermLib.ascii_run()
print(f'Dominguez Hills Observatory Controller V{version}')
print('\n' * 2)
selected_planet = get_planet()



t1 = time.time()
while True: # main program loop
    if time.time() - t1 >= 5: # stop after 5 seconds
        break
    get_azimuth(selected_planet, dh_observatory_lat, dh_observatory_lon)
    time.sleep(0.1)


exit = input('Enter any key to stop...')