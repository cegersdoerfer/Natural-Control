import RPi.GPIO as GPIO
import time

switch_pin1 = 8
switch_pin2 = 10
water_pin = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch_pin1, GPIO.OUT)
GPIO.setup(switch_pin2, GPIO.OUT)
GPIO.setup(water_pin, GPIO.OUT)

while True:
    current_time = time.localtime()
    if current_time.tm_hour < 8 or current_time.tm_hour >= 22:
        GPIO.output(switch_pin1, GPIO.HIGH)
        GPIO.output(switch_pin2, GPIO.HIGH)
        GPIO.output(water_pin, GPIO.HIGH)
    else:
        GPIO.output(switch_pin1, GPIO.LOW)
        GPIO.output(switch_pin2, GPIO.LOW)
    time.sleep(60)
