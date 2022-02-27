import RPi.GPIO as GPIO
import time

slidePin = 17


# Define a setup function for some setup
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(slidePin, GPIO.IN)


def main():
    while True:
        # slide switch high, led1 on
        if GPIO.input(slidePin) == 1:
            print ('on')
        # slide switch low, led2 on
        if GPIO.input(slidePin) == 0:
           print("off")
        time.sleep(0.5)

def destroy():
    # Turn off LED
  
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