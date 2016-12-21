#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit
import socket
from ast import literal_eval
import ROVCommands #Functions for Fwd, bckwd, etc...

recvBuf = ''

def recvNice(conn):
	global recvBuf
	while (recvBuf.find("\n")<0):
		data = conn.recv(1024)
		if (len(data) == 0):
			raise ValueError("No data recieved - client disconnected")
		print("data '"+`len(data)`+"'")
		recvBuf = recvBuf + data
	idx = recvBuf.find("\n")
	print("idx "+`idx`+" ; len = "+`len(recvBuf)`)
	ret = recvBuf[:idx]
	recvBuf = recvBuf[(idx+1):]
	return ret
def reprNice(obj):
	return repr(obj)+"\n"

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
downSpeed = 0.0
while True:	
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
	myMotor1.setSpeed(0) #UD Motor
	
	#literal_eval to turn the TCP message back into a dictionary.
	command = recvNice(conn) #Recieve data from socket
	dictCommand = literal_eval(command)
	if dictCommand["command"] == "FB": #Forward or Backward
		newSpeed1 = float(dictCommand["speed"]) #turn speed to a float
		if newSpeed1<0: #BOTH BACKWARD
			ROVCommands.ROVbackward(myMotor3, myMotor2, myMotor1)
		elif newSpeed1>0: #BOTH FORWARD	
			ROVCommands.ROVforward(myMotor3, myMotor2, myMotor1)
	elif dictCommand["command"] == "LR":
		newSpeed2 = float(dictCommand["speed"]) #Right or Left
		if newSpeed2<0: #LEFT
			ROVCommands.ROVleft(myMotor3, myMotor2, myMotor1)
		elif newSpeed2>0: #RIGHT
			ROVCommands.ROVright(myMotor3, myMotor2, myMotor1)
	elif dictCommand["command"] == "U":
		newSpeed3 = float(dictCommand["speed"]) #Up
		if newSpeed3>0: #UP
			ROVCommands.ROVup(myMotor3, myMotor2, myMotor1)
	elif dictCommand["command"] == "D":
		downSpeed = float(dictCommand["speed"]) #Down
		if downSpeed>0: #DOWN
			ROVCommands.ROVdown(myMotor3, myMotor2, myMotor1)
	else: #RELEASE
		ROVnoAction()


conn.close() #move this?

#FORWARD and BACKWARD
def ROVbackward(myMotor3, myMotor2, myMotor1):
	myMotor3.run(Adafruit_MotorHAT.BACKWARD), myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	print ("Backward!", newSpeed1)
	myMotor3.setSpeed(int(-newSpeed1)), myMotor2.setSpeed(int(-newSpeed1))
	conn.sendall(reprNice({"message":["Backward!"], "speed" : [newSpeed1]}))

def ROVforward(myMotor3, myMotor2, myMotor1):
	myMotor3.run(Adafruit_MotorHAT.FORWARD), myMotor2.run(Adafruit_MotorHAT.FORWARD)
	print ("Forward!", newSpeed1)
	myMotor3.setSpeed(int(newSpeed1)), myMotor2.setSpeed(int(newSpeed1))
	conn.sendall(reprNice({"message":["Forward!"], "speed" : [newSpeed1]}))
		
	#RIGHT and LEFT
def ROVleft(myMotor3, myMotor2, myMotor1):
	myMotor3.run(Adafruit_MotorHAT.FORWARD), myMotor2.run(Adafruit_MotorHAT.RELEASE)
	print (newSpeed2)
	myMotor3.setSpeed(int(-newSpeed2))
	print("Turning left!", newSpeed2)
	conn.sendall(reprNice({"message":["Turning Left!"], "speed" : [newSpeed2]}))
		
def ROVright(myMotor3, myMotor2, myMotor1):
	myMotor2.run(Adafruit_MotorHAT.FORWARD), myMotor3.run(Adafruit_MotorHAT.RELEASE)
	print (newSpeed2)
	myMotor2.setSpeed(int(newSpeed2))
	print("Turning right!", newSpeed2)
	conn.sendall(reprNice({"message":["Turning Right!"], "speed" : [newSpeed2]}))

	#UP and DOWN
def ROVup(myMotor3, myMotor2, myMotor1):
	myMotor1.run(Adafruit_MotorHAT.FORWARD)
	print("Going Up!", newSpeed3)
	conn.sendall(reprNice({"message":["Going Up!"], "speed" : [newSpeed3]}))

def ROVdown(myMotor3, myMotor2, myMotor1):
	myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	print("Going Down!", downSpeed)
	conn.sendall(reprNice({"message":["Going Down!"], "speed" : [downSpeed]}))

def ROVnoAction(myMotor3, myMotor2, myMotor1):
	#RELEASE ALL Motors
		myMotor3.run(Adafruit_MotorHAT.RELEASE), myMotor2.run(Adafruit_MotorHAT.RELEASE)
		print("No action, waiting for command.")
		conn.sendall(reprNice({"message":["No action, Waiting for command."], "speed" : [0.0]}))
