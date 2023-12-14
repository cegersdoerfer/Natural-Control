import RPi.GPIO as GPIO
import time
import datetime

switch_pin1 = 8
switch_pin2 = 10
water_pin = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch_pin1, GPIO.OUT)
GPIO.setup(switch_pin2, GPIO.OUT)
GPIO.setup(water_pin, GPIO.OUT)

# Initialize a variable to store the last day we activated the water pin
last_water_day = None

while True:
    current_time = time.localtime()

    # Check if it is night time
    if current_time.tm_hour < 8 or current_time.tm_hour >= 22:
        GPIO.output(switch_pin1, GPIO.HIGH)
        GPIO.output(switch_pin2, GPIO.HIGH)
    else:
        GPIO.output(switch_pin1, GPIO.LOW)
        GPIO.output(switch_pin2, GPIO.LOW)

    # Get today's date
    today = datetime.date.today()

    # Check if today is different from the last water day and if it is an alternate day
    if today != last_water_day and (last_water_day is None or (today - last_water_day).days >= 4):
        # Turn on the water pin
        GPIO.output(water_pin, GPIO.HIGH)
        time.sleep(10)  # Keep it on for 1 minute
        GPIO.output(water_pin, GPIO.LOW)
        last_water_day = today  # Update the last water day

    time.sleep(60)  # Wait for 1 minute before checking again
