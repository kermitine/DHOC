import serial
import time
from config.config import *


ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2) # Allow time for the serial connection to establish
def arduino_test_loop():
    while True:
        ser.write(b'1')
        print('Broadcasting LED on')
        time.sleep(1)
        ser.write(b'0')
        print('Broadcasting LED off')
        time.sleep(1)
