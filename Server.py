import Common
import socket
import sys
import traceback
import Motors

  # wait for connection from client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(Common.addrTuple)
s.listen(1)

newSpeed1 = 0.0
newSpeed2 = 0.0
newSpeed3 = 0.0
downSpeed = 0.0
conn = None
addr = None

# command wait loop
while True:
	if(conn is None):  # If we're not connected, stop the motors and wait for a connection
		Motors.stopAll()
		conn, addr = s.accept()
		print('Client connected from', addr)

	try:
		command = Common.recvNice(conn) #Recieve data from socket
		print("running cmd", command)
		Motors.setAll(command)
	except:
		print('-'*60)
		traceback.print_exc(file=sys.stdout)
		print('-'*60)
		print(":Dropping connection due to error")
		conn.close()
		conn = None
print("exit?")
	#literal_eval to turn the TCP message back into a dictionary.
	#dictCommand = literal_eval(command)
'''
	if dictCommand["command"] == "FB": #Forward or Backward
		newSpeed1 = float(dictCommand["speed"]) #turn speed to a float
		if newSpeed1<0: #BOTH BACKWARD
			ROVbackward(motor3, motor2, motor1)
		elif newSpeed1>0: #BOTH FORWARD	
			ROVforward(motor3, motor2, motor1)
	elif dictCommand["command"] == "LR":
		newSpeed2 = float(dictCommand["speed"]) #Right or Left
		if newSpeed2<0: #LEFT
			ROVleft(motor3, motor2, motor1)
		elif newSpeed2>0: #RIGHT
			ROVright(motor3, motor2, motor1)
	elif dictCommand["command"] == "U":
		newSpeed3 = float(dictCommand["speed"]) #Up
		if newSpeed3>0: #UP
			ROVup(motor3, motor2, motor1)
	elif dictCommand["command"] == "D":
		downSpeed = float(dictCommand["speed"]) #Down
		if downSpeed>0: #DOWN
			ROVdown(motor3, motor2, motor1)
	else: #RELEASE
		ROVnoAction()
'''
