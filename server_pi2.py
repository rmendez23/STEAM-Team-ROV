#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit
import socket
from ast import literal_eval
import ROVCommands #Functions for Fwd, bckwd, etc...

recvBuf = ''

def recvNice(conn):
	global recvBuf
	idx = recvBuf.find("\n")
	print("idx "+`idx`+" ; len = "+`len(recvBuf)`)
	if idx<1:
		data = conn.recv(1024)
		#print("data '"+data+"'")
		recvBuf = recvBuf + data
		return recvNice(conn)
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
	command = recvNice(s) #Recieve data from socket
	dictCommand = literal_eval(command)
	if dictCommand["command"] == "FB": #Forward or Backward
		newSpeed1 = float(dictCommand["speed"]) #turn speed to a float
		if newSpeed1<0: #BOTH BACKWARD
			ROVbackward()
		elif newSpeed1>0: #BOTH FORWARD	
			ROVforward()
	elif dictCommand["command"] == "LR":
		newSpeed2 = float(dictCommand["speed"]) #Right or Left
		if newSpeed2<0: #LEFT
			ROVleft()
		elif newSpeed2>0: #RIGHT
			ROVright()
	elif dictCommand["command"] == "U":
		newSpeed3 = float(dictCommand["speed"]) #Up
		if newSpeed3>0: #UP
			ROVup()
	elif dictCommand["command"] == "D":
		downSpeed = float(dictCommand["speed"]) #Down
		if downSpeed>0: #DOWN
			ROVdown()
	else: #RELEASE
		ROVnoAction()


conn.close() #move this?
