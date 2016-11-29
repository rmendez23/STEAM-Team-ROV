#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit
import socket
from ast import literal_eval
#do I need to import pygame?

recvBuf = ''

def recvNice(conn):
	global recvBuf
	idx = "\n".find(recvBuf)
	print("idx "+`idx`+" ; len = "+`len(recvBuf)`)
	if idx<1:
		data = conn.recv(1024)
		print("data '"+data+"'")
		recvBuf = recvBuf + data
		return recvNice(conn)
	ret = recvBuf[:idx]
	recvBuf = recvBuf[(idx+1):]
	return ret

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept() #establishes connection?
print('Connected by', addr)
newSpeed1 = 0.0
newSpeed2 = 0.0
newSpeed3 = 0.0
while True:
	#literal_eval to turn the TCP message back into a dictionary.
	command = recvNice(conn) #Recieve data from socket
	#print("'"+command+"'")
	dictCommand = literal_eval(command)
	if dictCommand["command"] == "FB": #Forward or Backward
		newSpeed1 = float(dictCommand["speed"]) #turn speed to a float
		print("'"+command+"'")
	elif dictCommand["command"] == "LR":
		newSpeed2 = float(dictCommand["speed"]) #Right or Left
		print("'"+command+"'")
	elif dictCommand["command"] == "UD":
		newSpeed3 = float(dictCommand["speed"]) #Up or Down
		print("'"+command+"'")
	#else if?
	#if not newSpeed: break #what should I do here?
	#conn.sendall(newSpeed1) # This sends the data recieved back to the client? Is this needed?
	
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

	myMotor1 = mh.getMotor(1) #Up and Down Motor

	# set the speed to start, from 0 (off) to 255 (max speed)
	myMotor3.setSpeed(0)

	myMotor2.setSpeed(0)

	myMotor1.setSpeed(0)

	#FORWARD and BACKWARD
	if newSpeed1<0: #BOTH BACKWARD

		myMotor3.run(Adafruit_MotorHAT.BACKWARD), myMotor2.run(Adafruit_MotorHAT.BACKWARD)

		print ("Backward!", newSpeed1)

		myMotor3.setSpeed(int(-newSpeed1)), myMotor2.setSpeed(int(-newSpeed1))
		
		conn.sendall(repr({"message":["Backward!"], "speed" : [newSpeed1]}))

	elif newSpeed1>0: #BOTH FORWARD

		myMotor3.run(Adafruit_MotorHAT.FORWARD), myMotor2.run(Adafruit_MotorHAT.FORWARD)

		print ("Forward!", newSpeed1)

		myMotor3.setSpeed(int(newSpeed1)), myMotor2.setSpeed(int(newSpeed1))
	#RIGHT and LEFT
	elif newSpeed2<0: #LEFT

		myMotor3.run(Adafruit_MotorHAT.FORWARD), myMotor2.run(Adafruit_MotorHAT.RELEASE)

		print (newSpeed2)

		myMotor3.setSpeed(int(-newSpeed2))

		print("Turning left!", newSpeed2)
	elif newSpeed2>0: #RIGHT

		myMotor2.run(Adafruit_MotorHAT.FORWARD), myMotor3.run(Adafruit_MotorHAT.RELEASE)

		print (newSpeed2)

		myMotor2.setSpeed(int(newSpeed2))

		print("Turning right!", newSpeed2)

	#UP and DOWN
	elif newSpeed3>0: #UP
		myMotor1.run(Adafruit_MotorHAT.FORWARD)
		print("Going Up!", newSpeed3)

	elif newSpeed3<0: #DOWN
		myMotor1.run(Adafruit_MotorHAT.BACKWARD)
		print("Going Down!", newSpeed3)

	else: #RELEASE
		myMotor3.run(Adafruit_MotorHAT.RELEASE), myMotor2.run(Adafruit_MotorHAT.RELEASE)
		print("No action, waiting for command.")
conn.close() #move this?
