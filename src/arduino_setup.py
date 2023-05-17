from pyduino import Arduino
import time

def setup(pin_number=11):
    a = Arduino() 
    time.sleep(1)

    ANALOG_PWM_PIN = pin_number

    a.set_pin_mode(ANALOG_PWM_PIN,'O')
    return a