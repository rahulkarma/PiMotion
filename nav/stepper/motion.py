from time import sleep
from .stepper_constants import *

class StepperMotion:
	def __init__(self, GPIO):
            self.step_mode_select = [STEPPER_m0, STEPPER_m1, STEPPER_m2]
            self.wheels_step = [BR_step, FR_step, BL_step, FL_step]
            self.wheels_dir = [BR_dir, FR_dir, BL_dir, FL_dir]
            out_pins = self.step_mode_select + self.wheels_step + self.wheels_dir
            
            [GPIO.setup(pin, GPIO.OUT) for pin in out_pins]

	"""
	TODO: Move forward and back

	Change Log
		[0.0.0] Rishav
			--- Created function
        Change Log
                [0.1.0] Jonathan
                        --- GPIO arg has been added to allow functionality of
                        the robots wheels. This allows us to manipulate IO pins.
                        Wheels have corrected names based off of their position.
        Change Log
                [0.2.0] Jonathan
                        --- Direction is now a boolean True or False. Since other
                        directions will be included later on, this is temporary.
                        ValueError Exception is now thrown when direction is not 
                        set to be True or False. Delay argument has been added 
                        that defaults to STEPPER_DELAY. This allows us to change 
                        the speed via the parameter.
	"""
	def mov(self, dir, distance, GPIO, delay=STEPPER_DELAY):
            distance = int(distance* STEPS_PER_INCH)
            
            try:
                #if FWD
                if dir:
                    for pin in [BR_dir, FR_dir]:
                        GPIO.output(pin, CW)
                    for pin in [BL_dir, FL_dir]:
                        GPIO.output(pin, CCW)
                #else if REV    
                elif not dir:
                    for pin in [BR_dir, FR_dir]:
                        GPIO.output(pin, CCW)
                    for pin in [BL_dir, FL_dir]:
                        GPIO.output(pin, CW)

                    for _ in range(distance):
                        [GPIO.output(x, GPIO.HIGH) for x in self.wheels_step]
                        sleep(delay)
                        [GPIO.output(x, GPIO.LOW) for x in self.wheels_step]
                        sleep(delay)
                
                else:
                    raise ValueError
            
            except ValueError:
                print("Error: Direction must be FWD or REV")


	# TODO: Turn left and right
	def turn(self, dir, degrees):
		pass

	# TODO: Strafe left and right
	def strafe(self, dir, distance):
		pass

	# TODO: Diagonal movement
	def diagonal_move(self, dir, distance):
		pass
