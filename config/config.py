version = '0.0.4'

# motor variables
motor_rpm = 3000
gear_ratio = 100
stepper_motor_steps = 200

# arduino variables
baud_rate = 9600
arduino_port = lambda port: 'COM' + str(port)
arduino_port_name = arduino_port(3)


# positional variabkes
dh_observatory_lat = 33.863907
dh_observatory_lon = -118.255190

# commonly used prompts
prompt_input_not_recognized = 'Input not recognized. Please try again.'