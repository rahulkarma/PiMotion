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
        [0.1.0] Jonathan
            --- GPIO arg has been added to allow functionality of the robots wheels. This allows us to manipulate IO pins. 
                Wheels have corrected names based off of their position.
        [0.2.0] Jonathan
            --- Direction is now a boolean True or False. Since other directions will be included later on, this is temporary.
                ValueError Exception is now thrown when direction is not set to be True or False. Delay argument has been added 
                that defaults to STEPPER_DELAY. This allows us to change the speed via the parameter.
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

    """
    For strafe right motion, FR=BL=fwd and BR=FL=rev
    For strafe left motion, FL=BR=fwd and FR=BL=rev

    Change Log
        [0.0.0] Rishav
            --- Created function
        [0.0.1] Rahul
            --- Added GPIO as input for motor movement
            --- Implemented left and right strafe movement
    """
    def strafe(self, dir, distance, GPIO):
        #run the motors iff the direction is left or right
        try:
        #strafe right
            if dir:
                [GPIO.output(pin, CW) for pin in [FL_dir, FR_dir]]
                [GPIO.output(pin, CCW) for pin in [BR_dir, BL_dir]]
        #else, strafe left
            elif not dir:
                [GPIO.output(pin, CW) for pin in [BL_dir, BR_dir]]
                [GPIO.output(pin, CCW) for pin in [FR_dir, FL_dir]]
            else:
                raise ValueError;
         #runs the motor for the given distance in inch   
            for _ in range(int(STEPS_PER_INCH_STRAFE * distance)):
                [GPIO.output(pin, GPIO.HIGH) for pin in self.wheels_step]
                sleep(STEPPER_DELAY)
                [GPIO.output(pin, GPIO.LOW) for pin in self.wheels_step]
                sleep(STEPPER_DELAY)
        
        except ValueError:
            print('Direction has to be LEFT or RIGHT')
        

    # TODO: Diagonal movement
    def diagonal_move(self, dir, distance):
        pass
