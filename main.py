from argparse import ArgumentParser
import RPi.GPIO as GPIO
from motion import*
from motion import StepperMotion
from stepper_constants import STEP_MODE_SELECT


def main():
    parser = ArgumentParser(description='Select modes on the robot')
    parser.add_argument("-m", "--motor_select", dest="motor_select", default="stepper", help="Stepper or DC")
    parser.add_argument("-d", "--stepper_delay", dest="stepper_delay", type=float, default=0.005, help="Delay for stepper motors")
    parser.add_argument("-f", "--fwd_dist", dest="dist", type=int, default=5, help="Distance to move forward")

    args = parser.parse_args()
    motor_select = args.motor_select
    stepper_delay = args.stepper_delay
    fwd_dist = args.dist

    # Refering to pins by the "Broadcom SOC channel".
    GPIO.setmode(GPIO.BCM)

    # Initialize stepper motion object
    step_motion = StepperMotion(GPIO)
    
    # Initiallize motor controller board. Set step to quater step
    [GPIO.output(pin, GPIO.HIGH) for pin in STEP_MODE_SELECT]

    # TODO: Example call
    #step_motion.strafe(LEFT, 7, GPIO)
    step_motion.diagonal_move(LEFT, FWD, 14, GPIO)
    #step_motion.mov(0, 6, GPIO)
    # Close motor controller board.
    [GPIO.output(pin, GPIO.LOW) for pin in STEP_MODE_SELECT]

    GPIO.cleanup()

if __name__ == "__main__":
    main()
