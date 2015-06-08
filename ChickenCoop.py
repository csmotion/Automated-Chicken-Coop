import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setwarnings(False)

relay_OFF = 1
relay_ON = 0

motor_OFF = 0
motor_ON = 1

dir_open = 0
dir_closed = 1

door_timeout_sec = 12

relay_pins = {'socket1':6, 'socket2':13, 'socket3':19, 'socket4':26}
motor_pins = {'dir':22, 'enable':17, 'brake':27}
limit_pins = {'open':24, 'closed':23}

# INITIALIZE GPIO
#-----------------------------------------------------------------#
# choose BCM port numbering
GPIO.setmode(GPIO.BCM)

# setup relay pins
for pin in relay_pins.values():
	GPIO.setup(pin, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
	GPIO.output(pin, relay_OFF)

# setup motor pins
for pin in motor_pins.values():
	GPIO.setup(pin, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
	GPIO.output(pin, motor_OFF)

# setup limit switch pins
for pin in limit_pins.values():
	GPIO.setup(pin, GPIO.IN)

#FUNCTIONS
#-----------------------------------------------------------------#
def testRelays():
	for pin in relay_pins.values():
		print str(pin) + "\n"
		GPIO.output(pin, 0)
		sleep(1)
		GPIO.output(pin, 1)
		sleep(1)

def testMotor():
	GPIO.output(motor_pins['dir'], 0)
	GPIO.output(motor_pins['enable'], 1)
	sleep(1)
	GPIO.output(motor_pins['dir'], 1)
	sleep(1)
	GPIO.output(motor_pins['enable'], 0)

def testLimits():
	for pin in limit_pins.values():
		state = GPIO.input(pin)
		print "Limit state = " + str(state)

def doorStatus():
	open = not GPIO.input(limit_pins['open'])
	closed = not GPIO.input(limit_pins['closed'])

	if (open==True) and (closed==True):
		return 'fault'
	elif (open==True):
		return 'open'
	elif (closed==True):
		return 'closed'
	else: 
		return 'unknown'

def openDoor():
	if (doorStatus() != 'open'):
		GPIO.output(motor_pins['dir'],dir_open)
		GPIO.output(motor_pins['enable'], 1)
		
		elapsed = 0
		start = time()
		while((doorStatus() != 'open') and elapsed < door_timeout_sec):
			elapsed = time() - start
			pass
		GPIO.output(motor_pins['enable'], 0)
		return doorStatus()

def closeDoor():
	if (doorStatus() != 'closed'):
		GPIO.output(motor_pins['dir'],dir_closed)
		GPIO.output(motor_pins['enable'], 1)

		elapsed = 0
		start = time()
		while(doorStatus() != 'closed'):
			elapsed = time() - start
			pass
		GPIO.output(motor_pins['enable'], 0)
		return doorStatus()

#-----------------------------------------------------------------#
if __name__ == "__main__":
	#testRelays()
	#testMotor()
	print doorStatus()
	print openDoor()
	sleep(1)
	print closeDoor()
