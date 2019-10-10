from time import sleep
from stepper_constants import *

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
        
        distance = int(distance * STEPS_PER_INCH)
        
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
        while (dir == LEFT or dir == RIGHT):
        #strafe right
            if dir == RIGHT:
                [GPIO.output(pin, CW) for pin in [FL_dir, FR_dir]]
                [GPIO.output(pin, CCW) for pin in [BR_dir, BL_dir]]
        #else, strafe left
            elif dir == LEFT:
                [GPIO.output(pin, CW) for pin in [BL_dir, BR_dir]]
                [GPIO.output(pin, CCW) for pin in [FR_dir, FL_dir]]
         #runs the motor for the given distance in inch   
            for _ in range(int(STEPS_PER_INCH_STRAFE * distance)):
                [GPIO.output(pin, GPIO.HIGH) for pin in self.wheels_step]
                sleep(STEPPER_DELAY)
                [GPIO.output(pin, GPIO.LOW) for pin in self.wheels_step]
                sleep(STEPPER_DELAY)
            break
        #If the direction is not right or left, give the warning
        if (dir != RIGHT and dir != LEFT):
            print('Direction has to be LEFT or RIGHT')
    

    # TODO: Diagonal movement
    def diagonal_move(self, dir, motion, distance, GPIO):
        distance = int(distance * STEPS_PER_INCH)
        if dir == RIGHT:
            if motion == FWD:
                GPIO.output(FL_dir, CW)
                GPIO.output(BR_dir, CCW)
            elif motion == REV:
                GPIO.output(FL_dir, CCW)
                GPIO.output(BR_dir, CW)
            for _ in range(distance):
                [GPIO.output(pin, GPIO.HIGH) for pin in [FL_step, BR_step]]
                sleep(STEPPER_DELAY)
                [GPIO.output(pin, GPIO.LOW) for pin in  [FL_step, BR_step]]
                sleep(STEPPER_DELAY)
        elif dir == LEFT:
            if motion == FWD:
                GPIO.output(BL_dir, CW)
                GPIO.output(FR_dir, CCW)
            elif motion == REV:
                GPIO.output(BL_dir, CCW)
                GPIO.output(FR_dir, CW)
            for _ in range(distance):
                [GPIO.output(pin, GPIO.HIGH) for pin in [FR_step, BL_step]]
                sleep(STEPPER_DELAY)
                [GPIO.output(pin, GPIO.LOW) for pin in  [FR_step, BL_step]]
                sleep(STEPPER_DELAY)
        
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
