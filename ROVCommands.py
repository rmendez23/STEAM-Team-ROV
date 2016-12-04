#FORWARD and BACKWARD
def ROVbackward():
	myMotor3.run(Adafruit_MotorHAT.BACKWARD), myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	print ("Backward!", newSpeed1)
	myMotor3.setSpeed(int(-newSpeed1)), myMotor2.setSpeed(int(-newSpeed1))
	conn.sendall(reprNice({"message":["Backward!"], "speed" : [newSpeed1]}))

def ROVforward():
	myMotor3.run(Adafruit_MotorHAT.FORWARD), myMotor2.run(Adafruit_MotorHAT.FORWARD)
	print ("Forward!", newSpeed1)
	myMotor3.setSpeed(int(newSpeed1)), myMotor2.setSpeed(int(newSpeed1))
	conn.sendall(reprNice({"message":["Forward!"], "speed" : [newSpeed1]}))
		
	#RIGHT and LEFT
def ROVleft():
	myMotor3.run(Adafruit_MotorHAT.FORWARD), myMotor2.run(Adafruit_MotorHAT.RELEASE)
	print (newSpeed2)
	myMotor3.setSpeed(int(-newSpeed2))
	print("Turning left!", newSpeed2)
	conn.sendall(reprNice({"message":["Turning Left!"], "speed" : [newSpeed2]}))
		
def ROVright():
	myMotor2.run(Adafruit_MotorHAT.FORWARD), myMotor3.run(Adafruit_MotorHAT.RELEASE)
	print (newSpeed2)
	myMotor2.setSpeed(int(newSpeed2))
	print("Turning right!", newSpeed2)
	conn.sendall(reprNice({"message":["Turning Right!"], "speed" : [newSpeed2]}))

	#UP and DOWN
def ROVup():
	myMotor1.run(Adafruit_MotorHAT.FORWARD)
	print("Going Up!", newSpeed3)
	conn.sendall(reprNice({"message":["Going Up!"], "speed" : [newSpeed3]}))

def ROVdown():
	myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	print("Going Down!", downSpeed)
	conn.sendall(reprNice({"message":["Going Down!"], "speed" : [downSpeed]}))

def ROVnoAction():
	else: #RELEASE ALL Motors
		myMotor3.run(Adafruit_MotorHAT.RELEASE), myMotor2.run(Adafruit_MotorHAT.RELEASE)
		print("No action, waiting for command.")
		conn.sendall(reprNice({"message":["No action, Waiting for command."], "speed" : [0.0]}))
