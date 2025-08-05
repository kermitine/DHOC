# CONVERT AZIMUTH ANGLE TO MOTOR STEPS
# https://www.amazon.com/Nema-23-Planetary-Gearbox-100/dp/B094R8Q2F1?th=1
# NEMA 23- 200 steps per revolution. * 100-1 gearbox ratio makes it 20,000 steps per revolution
# 200steps/360degrees = 1.8 degrees/step. With gearbox, 0.018 degrees/step
#
def degrees_to_steps(degrees, steps, gear_ratio):
    pass