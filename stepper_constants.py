import math
# Stepper mode select
STEPPER_m0 = 17
STEPPER_m1 = 27
STEPPER_m2 = 22

STEP_MODE_SELECT = [STEPPER_m0, STEPPER_m1, STEPPER_m2]

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

CW = 1                           # Clockwise rotation
CCW = 0                          # Counter-clockwise rotation
STEPS_PER_REVOLUTION = 800       # Steps per Revolution (360/1.8) * 4. Multiply by 4 because quarter step.
DISTANCE = 60*math.pi/25.4
STEPS_PER_INCH = STEPS_PER_REVOLUTION/DISTANCE
STEPPER_DELAY = 0.0005
STEPS_PER_INCH_STRAFE = STEPS_PER_REVOLUTION/(DISTANCE*0.8727587968457)  # Calibrates steps_per_inch for strafe motion.

#For Strafe motion
LEFT = 0
RIGHT = 1

#For diagonal motion
FWD = "FORWARD"
REV = "REVERSE"

