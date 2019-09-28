# Stepper mode select
STEPPER_m0 = 17
STEPPER_m1 = 27
STEPPER_m2 = 22

# First wheel GPIO Pin
WHEEL1_step = 21
WHEEL1_dir = 20

# Second wheel GPIO Pin
WHEEL2_step = 11
WHEEL2_dir = 10

# Third wheel GPIO Pin
WHEEL3_step = 7
WHEEL3_dir = 8

# Fourth wheel GPIO Pin
WHEEL4_step = 24
WHEEL4_dir = 23

CW = 1 			                 # Clockwise rotation
CCW = 0 		                 # Counter-clockwise rotation
STEPS_PER_REVOLUTION = 800 		 # Steps per Revolution (360/1.8) * 4. Multiply by 4 because quarter step.

STEPPER_DELAY = 0.0005
