from config.config import *

def get_planet():
    while True:
        target_planet = input("Please enter target planet: ")
        if target_planet is None or target_planet.strip() == '':
            print(prompt_input_not_recognized)
        else:
            try:
                target_planet = str(target_planet.strip())
                break
            except ValueError:
                print(prompt_input_not_recognized)
    return (target_planet.capitalize() + ' Barycenter')