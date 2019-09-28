from time import sleep
import RPi.GPIO as GPIO
from stepper_constants import *

GPIO.setmode(GPIO.BCM)

step_mode_select = [STEPPER_m0, STEPPER_m1, STEPPER_m2]
wheels_step = [WHEEL1_step, WHEEL2_step, WHEEL3_step, WHEEL4_step]
wheels_dir = [WHEEL1_dir, WHEEL2_dir, WHEEL3_dir, WHEEL4_dir]

# Set GPIO pinouts
out_pins = step_mode_select + wheels_step + wheels_dir
for pin in out_pins:
	GPIO.setup(pin, GPIO.OUT)

step_count = STEPS_PER_REVOLUTION * 20

for pin in wheels_dir:
	GPIO.output(pin, CW)

for pin in step_mode_select:
	GPIO.output(pin, GPIO.HIGH)

sleep(1)

for x in range(step_count):
	[GPIO.output(x, GPIO.HIGH) for x in wheels_step]
	sleep(STEPPER_DELAY)
	[GPIO.output(x, GPIO.LOW) for x in wheels_step]
	sleep(STEPPER_DELAY)

sleep(.5)

for pin in wheels_dir:
	GPIO.output(pin, CCW)

for pin in step_mode_select:
	GPIO.output(pin, GPIO.LOW)
