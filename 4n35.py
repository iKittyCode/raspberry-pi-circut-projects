import RPi.GPIO as GPIO
import time

Pin_4N35 = 17

# Define a setup function for some setup
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Pin_4N35, GPIO.OUT, initial=GPIO.LOW)

# Define a main function for main process
def main():
    while True:
        # Turn off LED
        GPIO.output(Pin_4N35, GPIO.HIGH)
        time.sleep(0.5)
        # Turn on LED
        GPIO.output(Pin_4N35, GPIO.LOW)
        time.sleep(0.5)

def destroy():
    # Turn off LED
    GPIO.output(Pin_4N35, GPIO.HIGH)
    # Release resource
    GPIO.cleanup()

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        main()
    # When 'Ctrl+C' is pressed, the child program
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()