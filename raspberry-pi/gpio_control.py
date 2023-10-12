import RPi.GPIO as GPIO
import time

switch_pin = 8


GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch_pin, GPIO.OUT)

while True:
    current_time = time.localtime()
    if current_time.tm_hour <= 8 and current_time.tm_hour >= 20:
        GPIO.output(switch_pin, GPIO.HIGH)
    else:
        GPIO.output(switch_pin, GPIO.LOW)
    time.sleep(60)