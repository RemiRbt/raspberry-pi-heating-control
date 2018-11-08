import RPi.GPIO as GPIO
import time
import os

# Setting GPIO pins
BUTTON_PIN = 21

while True:
    # Setting modes here to prevent others action to clean GPIO's pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # If button is pressed then 'sudo halt'
    input_state = GPIO.input(BUTTON_PIN)
    if input_state == False:
        os.system("sudo halt")
        time.sleep(0.2)
        GPIO.cleanup()
