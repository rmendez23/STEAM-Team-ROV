#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit
import socket
#do I need to import pygame?

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept() #establishes connection?
print('Connected by', addr)
while True:
	newSpeed = conn.recv(1024) #recieving data? data is newSpeed?
	if not newSpeed: break
	conn.sendall(newSpeed) # This sends the data recieved back to the client?
	
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

	if newSpeed<0:
		myMotor.run(Adafruit_MotorHAT.BACKWARD)
		print (newSpeed) #dont need?
		myMotor.setSpeed(int(-newSpeed))

	if newSpeed>0:
		myMotor.run(Adafruit_MotorHAT.FORWARD)
		print (newSpeed)myMotor.setSpeed(int(newSpeed))
conn.close() #move this?
