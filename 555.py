import RPi.GPIO as GPIO
import time

SigPin = 18

g_count = 0

def count(ev=None):
    global g_count
    g_count += 1

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SigPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(SigPin, GPIO.RISING, callback=count) # wait for rasing

def main():
    while True:
        print ('g_count = %d' % g_count)
        time.sleep(0.01)

def destroy():
    GPIO.cleanup()    # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        main()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()