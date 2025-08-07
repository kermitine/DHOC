import serial
import time
from config.config import *



def arduino_test_loop(main_window_object):
    # Open the serial connection
    main_window_object.send_to_console(f'Opening serial at {arduino_port} on baud {baud_rate}')
    ser = serial.Serial(arduino_port, baud_rate, timeout=1) 
    time.sleep(2) # Allow time for the serial connection to establish

    print("Sending '1' to turn LED ON...")
    ser.write(b'1') # Send '1' as a byte string

    time.sleep(2) # Wait for 2 seconds

    print("Sending '0' to turn LED OFF...")
    ser.write(b'0') # Send '0' as a byte string

    print(f'Closing serial at {arduino_port} on baud {baud_rate}...')
    ser.close()
