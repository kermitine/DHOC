import serial
import time
from config.config import *



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
