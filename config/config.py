version = '0.0.4'

motor_settings = {
    'rpm': 3000,
    'gear_ratio': 100,
    'stepper_motor_steps': 200
}

arduino_settings = {
    'port': 'COM3',
    'baud_rate': 9600,
    'port_number': 3
}

azimuth_settings = { # defaults are the latitude and longitude for CSUDH Observatory
    'latitude': 33.863907, 
    'longitude': -118.255190,
    'planet': 'Mars'
}

# commonly used prompts
prompt_input_not_recognized = 'Input not recognized. Please try again.'