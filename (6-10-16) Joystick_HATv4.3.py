#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit
import serial
import pygame
import time

'''
Gets joystick data and prints it
'''
pygame.init()
#joystick.init()
hat_number = get_numhats() - 1
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

myMotor3 = mh.getMotor(3)

myMotor2 = mh.getMotor(2)

myMotor1 = mg.getMotor(1) #Elevation Motor

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor3.setSpeed(0)

myMotor2.setSpeed(0)

myMotor1.setSpeed(0)

try:
	while (True):
		#pygame.event.pump()
		pygame.event.wait()
		myEvents = pygame.event.get()
		for e in myEvents:
			if e.type = pygame.JOYAXISMOTION:
				
				newSpeed1 = -250.0*j.get_axis(4)
			
				newSpeed2 = -250.0*j.get_axis(0)
				
				#FORWARD and BACKWARD
				if newSpeed1<0: #BOTH BACKWARD
					
					myMotor3.run(Adafruit_MotorHAT.BACKWARD), myMotor2.run(Adafruit_MotorHAT.BACKWARD)

					print ("Backward!", newSpeed1)
			   
					myMotor3.setSpeed(int(-newSpeed1)), myMotor2.setSpeed(int(-newSpeed1))
			
				else if newSpeed1>0: #BOTH FORWARD

					myMotor3.run(Adafruit_MotorHAT.FORWARD), myMotor2.run(Adafruit_MotorHAT.FORWARD)

					print ("Forward!", newSpeed1)
			   
					myMotor3.setSpeed(int(newSpeed1)), myMotor2.setSpeed(int(newSpeed1))
				#RIGHT and LEFT
				else if newSpeed2<0: #LEFT
					
					myMotor3.run(Adafruit_MotorHAT.FORWARD), myMotor2.run(Adafruit_MotorHAT.RELEASE)

					print (newSpeed2)
			   
					myMotor3.setSpeed(int(-newSpeed2))
					
					print("Turning left!", newSpeed2)
				else if newSpeed2>0: #RIGHT
					
					myMotor2.run(Adafruit_MotorHAT.FORWARD), myMotor3.run(Adafruit_MotorHAT.RELEASE)

					print (newSpeed2)
			   
					myMotor2.setSpeed(int(newSpeed2))
					
					print("Turning right!", newSpeed2)
			if e.type = pygame.JOYHATMOTION:
					newSpeed3 = -250.0*j.get_hat(hat_number)[1] #y position tuple of j.get_hat
					
					#UP and DOWN
					else if newSpeed3>0: #UP
						myMotor1.run(Adafruit_MotorHAT.FORWARD)
						print("Going Up!", newSpeed3)
					
					else if: newSpeed<0: #DOWN
						myMotor1.run(Adafruit_MotorHAT.BACKWARD)
						print("Going Down!", newSpeed3)
					
					else: #RELEASE
						myMotor3.run(Adafruit_MotorHAT.RELEASE), myMotor2.run(Adafruit_MotorHAT.RELEASE)
						print("No action, waiting for command.")
except KeyboardInterrupt:
    j.quit()
