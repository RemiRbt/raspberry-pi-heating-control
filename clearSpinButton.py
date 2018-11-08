import RPi.GPIO as GPIO
import time
import sys

# Setting GPIO pins
BUTTON_PIN = 20
SERVO_CONTROL_PIN = 23

# Setting servo vars
PWM_FREQUENCY = 50
END_POSITION = 5

while True:
    # Setting modes here to prevent others action to clean GPIO's pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SERVO_CONTROL_PIN, GPIO.OUT)
    pwm = GPIO.PWM(SERVO_CONTROL_PIN, PWM_FREQUENCY)
    # If button is pressed then rotate the motor
    input_state = GPIO.input(BUTTON_PIN)
    if input_state == False:
        pwm.start(END_POSITION)
        # Sleep to avoid flooding script if button is still pressed
        time.sleep(0.5)
        pwm.stop()
        GPIO.cleanup()
