#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit

import serial
import pygame
import time

#serialPort = '/dev/tty.usbserial-A7004Jg4' # Arduino Mega
#serialPort = '/dev/tty.usbmodemfd121'       # Arduino Uno
#baudRate = 9600

# Open Serial Connection to Arduino Board
#ser = serial.Serial(serialPort, baudRate, timeout=1);

'''
Gets joystick data and prints it
'''
pygame.init()
#joystick.init()
j = pygame.joystick.Joystick(0)
j.init()
print 'Initialized Joystick : %s' % j.get_name()

# Keeps a history of buttons pressed so that one press does
# not send multiple presses to the Arduino Board
button_history = [0,0,0,0,0,0,0,0,0,0,0,0]

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myMotor = mh.getMotor(3)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor.setSpeed(0)
try:
	while (True):
		pygame.event.pump()
		newSpeed = -250.0*j.get_axis(4)
		print (newSpeed)
		
		if newSpeed<0:
			
			myMotor.run(Adafruit_MotorHAT.BACKWARD)

			print (newSpeed)
	   
			myMotor.setSpeed(int(-newSpeed))
	
		if newSpeed>0:

			myMotor.run(Adafruit_MotorHAT.FORWARD)

			print (newSpeed)
	   
			myMotor.setSpeed(int(newSpeed))
	   
except KeyboardInterrupt:
    j.quit()





# try:
#while (True):
#    speed = 250*j.get_axis(4)
#    print (speed)
#	print "Forward! "
#	myMotor.run(Adafruit_MotorHAT.FORWARD)

#	print "\tSpeed up..."
#	for i in range (1,250)
#		myMotor.setSpeed(int(i*250))

#	print (int((250*(j.get_axis(4)))))
        
# except KeyboardInterrupt:
#    j.quit()