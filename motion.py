from time import sleep
import RPi.GPIO as GPIO

# Micheal said these need to be high to set step 
L_PURPLE = 17
L_GREY = 27
L_WHITE = 22

# First wheel GPIO Pin
wheel1_step = 21
wheel1_dir = 20

# Second wheel GPIO Pin
wheel2_step = 11
wheel2_dir = 10

CW = 1 			# Clockwise rotation
CCW = 0 		# Counter-clockwise rotation
SPR = 800 		# Steps per Revolution (360/1.8) * 4. Multiply by 4 because quarter step.

GPIO.setmode(GPIO.BCM)

# Set GPIO pinouts
out_pins = [L_PURPLE, L_GREY, L_WHITE, wheel1_step, wheel1_dir, wheel2_step, wheel2_dir]
for pin in out_pins:
	GPIO.setup(pin, GPIO.OUT)

for pin in [wheel1_dir, wheel2_dir]:
	GPIO.output(pin, CW)

step_count = SPR * 10
delay = 0.00005

for pin in [L_PURPLE, L_GREY, L_WHITE]:
	GPIO.output(pin, GPIO.HIGH)	

sleep(2)

for x in range(step_count):
	GPIO.output(wheel1_step, GPIO.HIGH)
	GPIO.output(wheel2_step, GPIO.HIGH)
	sleep(delay)
	GPIO.output(wheel1_step, GPIO.LOW)
	GPIO.output(wheel2_step, GPIO.LOW)
	sleep(delay)
	
sleep(.5)

for pin in [wheel1_dir, wheel2_dir]:
	GPIO.output(pin, CCW)	

for pin in [L_PURPLE, L_GREY, L_WHITE]:
	GPIO.output(pin, GPIO.LOW)
