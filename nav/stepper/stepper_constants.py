import math
# Stepper mode select
STEPPER_m0 = 17
STEPPER_m1 = 27
STEPPER_m2 = 22

# First wheel GPIO Pin
BR_step = 21
BR_dir = 20

# Second wheel GPIO Pin
FR_step = 11
FR_dir = 10

# Third wheel GPIO Pin
BL_step = 7
BL_dir = 8

# Fourth wheel GPIO Pin
FL_step = 24
FL_dir = 23

#Direction constants
FWD = True
REV = False

CW = 1 			                 # Clockwise rotation
CCW = 0 		                 # Counter-clockwise rotation
STEPS_PER_REVOLUTION = 800 		 # Steps per Revolution (360/1.8) * 4. Multiply by 4 because quarter step.
DISTANCE = 60*math.pi/25.4
STEPS_PER_INCH = STEPS_PER_REVOLUTION/DISTANCE
STEPPER_DELAY = 0.0005
