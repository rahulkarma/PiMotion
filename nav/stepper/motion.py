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
	"""
	def mov(self, dir, distance, GPIO):
            for pin in self.step_mode_select:
                GPIO.output(pin, GPIO.HIGH)
                
            distance = int(distance* STEPS_PER_INCH)
            sleep(1)
                
            if(dir == 0):
                for pin in [BR_dir, FR_dir]:
                    GPIO.output(pin, CCW)
                for pin in [BL_dir, FL_dir]:
                    GPIO.output(pin, CW)
                    
            if(dir == 1):
                for pin in [BR_dir, FR_dir]:
                    GPIO.output(pin, CW)
                for pin in [BL_dir, FL_dir]:
                    GPIO.output(pin, CCW)

                for _ in range(distance):
                    [GPIO.output(x, GPIO.HIGH) for x in self.wheels_step]
                    sleep(STEPPER_DELAY)
                    [GPIO.output(x, GPIO.LOW) for x in self.wheels_step]
                    sleep(STEPPER_DELAY)
                
                sleep(.5)
                
                for pin in self.step_mode_select:
                    GPIO.output(pin, GPIO.LOW)

	# TODO: Turn left and right
	def turn(self, dir, degrees):
		pass

	# TODO: Strafe left and right
	def strafe(self, dir, distance):
		pass

	# TODO: Diagonal movement
	def diagonal_move(self, dir, distance):
		pass
