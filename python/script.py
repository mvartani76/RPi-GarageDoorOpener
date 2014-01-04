import webiopi

GPIO = webiopi.GPIO

GARAGE1 = 17 # GPIO pin using BCM numbering
GARAGE2 = 21 # GPIO pin using BCM numbering

# setup function is automatically called at WebIOPi startup
def setup():
	# set the GPIO used by the garage doors to output
	GPIO.setFunction(GARAGE1, GPIO.OUT)
	GPIO.setFunction(GARAGE2, GPIO.OUT)

def destroy():
	GPIO.digitalWrite(GARAGE1, GPIO.LOW)
	GPIO.digitalWrite(GARAGE2, GPIO.LOW)

