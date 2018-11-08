import RPi.GPIO as GPIO
import time


# Setting GPIO pin
SERVO_CONTROL_PIN = 23

# Setting servo vars
PWM_FREQUENCY = 50
END_POSITION = 10

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SERVO_CONTROL_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_CONTROL_PIN, PWM_FREQUENCY)
pwm.start(END_POSITION)
# Sleep to avoid flooding script
time.sleep(0.5)
pwm.stop()
GPIO.cleanup()
