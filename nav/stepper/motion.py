from time import sleep
from .stepper_constants import *

class StepperMotion:
	def __init__(self, GPIO):
		self.step_mode_select = [STEPPER_m0, STEPPER_m1, STEPPER_m2]
		self.wheels_step = [WHEEL1_step, WHEEL2_step, WHEEL3_step, WHEEL4_step]
		self.wheels_dir = [WHEEL1_dir, WHEEL2_dir, WHEEL3_dir, WHEEL4_dir]

		out_pins = self.step_mode_select + self.wheels_step + self.wheels_dir

		[GPIO.setup(pin, GPIO.OUT) for pin in out_pins]

	"""
	TODO: Move forward and back

	Change Log
		[0.0.0] Rishav
			--- Created function
	"""
	def mov(self, dir, distance):
		print(dir, distance)

	# TODO: Turn left and right
	def turn(self, dir, degrees):
		pass

	# TODO: Strafe left and right
	def strafe(self, dir, distance):
		pass

	# TODO: Diagonal movement
	def diagonal_move(self, dir, distance):
		pass
