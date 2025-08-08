"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the DHOC project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""


# Test to see if PySerial is working and communicating with the Arduino board.
# INSTRUCTIONS:
# 1) Flash "test_sketch_led.ino" onto Arduino. 
# 2) Connect led to digital pin 12 on Arduino
# 3) Close IDE so serial monitor doesn't interfere with PySerial.
# 4) Run this code. Ensure that the port and baud rate is correct (if not, edit in config.settings)
# 5) LED should turn on for 2 secs, then off.


import serial
import time
from config.settings import *

def arduino_test_loop(main_window_object):
    # Open the serial connection
    try:
        ser = serial.Serial(arduino_settings['port'], arduino_settings['baud_rate'], timeout=1)
    except:
        main_window_object.send_to_console('ERROR: Serial connection failure.')
        return None
    time.sleep(2) # Allow time for the serial connection to establish

    print("Sending '1' to turn LED ON...")
    ser.write(b'1') # Send '1' as a byte string

    time.sleep(2) # Wait for 2 seconds

    print("Sending '0' to turn LED OFF...")
    ser.write(b'0') # Send '0' as a byte string

    print(f'Closing serial at {arduino_settings['port']} on baud {arduino_settings['baud_rate']}...')
    ser.close()
    main_window_object.send_to_console(f'Closing serial at {arduino_settings['port']} on baud {arduino_settings['baud_rate']}')
