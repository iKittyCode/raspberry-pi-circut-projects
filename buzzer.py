import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
BeepPin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BeepPin, GPIO.OUT, initial=GPIO.LOW)
    

def main():
    for i in range(0, 12):
        # Buzzer on (Beep)
        GPIO.output(BeepPin, GPIO.HIGH)
        time.sleep(0.1)
        # Buzzer off
        GPIO.output(BeepPin, GPIO.LOW)
        time.sleep(0.1)
    
def destroy():
    # Turn off buzzer
    GPIO.output(BeepPin, GPIO.LOW)
   
    

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    
    main()
    destroy()