from gpiozero import Button
from subprocess import call
#pin at gpio 18 bcm
button = Button(18)

button.wait_for_press()
call(['/usr/bin/python3', 'servo.py'])

