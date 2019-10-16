from argparse import ArgumentParser
import RPi.GPIO as GPIO
from nav.stepper.motion import StepperMotion

def main():
    parser = ArgumentParser(description='Select modes on the robot')
    parser.add_argument("-m", "--motor_select", dest="motor_select", default="stepper", help="Stepper or DC")
    parser.add_argument("-d", "--stepper_delay", dest="stepper_delay", type=float, default=0.005, help="Delay for stepper motors")
    parser.add_argument("-f", "--fwd_dist", dest="dist", type=int, default=None, help="Distance to move forward")

    args = parser.parse_args()
    motor_select = args.motor_select
    stepper_delay = args.stepper_delay
    fwd_dist = args.dist

    # Refering to pins by the "Broadcom SOC channel".
    GPIO.setmode(GPIO.BCM)

    # Initialize stepper motion object
    step_motion = StepperMotion(GPIO)
    
    # Motor controller
    for pin in self.step_mode_select:
        GPIO.output(pin, GPIO.HIGH)
    
    sleep(1)

    # TODO: Example call
    step_motion.mov(FWD, fwd_dist, GPIO) #FWD is True, changed from int 1. REV = False

    GPIO.cleanup()

if __name__ == "__main__":
    main()
