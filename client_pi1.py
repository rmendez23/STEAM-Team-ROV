#test_client1.py

#!/usr/bin/python
#Joystick stuff
import serial
import pygame
import time
import sys
from ast import literal_eval
import socket

'''
Gets joystick data and prints it
'''
pygame.init()
#joystick.init()
j = pygame.joystick.Joystick(0)
j.init()
#hat_number = j.get_numhats() - 1
print 'Initialized Joystick : %s' % j.get_name()

# Keeps a history of buttons pressed so that one press does
# not send multiple presses to the Arduino Board
button_history = [0,0,0,0,0,0,0,0,0,0,0,0]

recvBuf = ''
def recvNice(conn):
	global recvBuf
	idx = recvBuf.find("\n")
	print("idx "+`idx`+" ; len = "+`len(recvBuf)`)
	if idx<1:
		data = conn.recv(1024) #s.recv(1024)?
		#print("data '"+data+"'")
		recvBuf = recvBuf + data
		return recvNice(conn)
	ret = recvBuf[:idx]
	recvBuf = recvBuf[(idx+1):]
	return ret

def reprNice(obj):
	return repr(obj)+"\n"

try:
	#client socket		
	host = '10.66.66.1' #socket.gethostname() change to IP of server   
	port = 12345                   # The same port as used by the server
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object
	s.connect((host, port)) #connect to server
	while (True):
		try:
			#pygame.event.pump()
			pygame.event.wait()
			myEvents = pygame.event.get()
			for e in myEvents:
				if e.type == pygame.JOYAXISMOTION:
					newSpeed1 = -250.0*j.get_axis(4)
					newSpeed2 = 250.0*j.get_axis(0)
					s.sendall(reprNice({"command" : "FB", "speed" : newSpeed1}))
					s.sendall(reprNice({"command" : "LR", "speed" : newSpeed2}))
					
				if e.type == pygame.JOYBUTTONDOWN:
					newSpeed3 = 250.0*j.get_button(3) #button 
					downSpeed = 250.0*j.get_button(0) #down button
					s.sendall(reprNice({"command" : "U", "speed" : newSpeed3}))
					s.sendall(reprNice({"command" : "D", "speed" : downSpeed}))
					
				serverMsg = recvNice(1024) #Not sure if I did this right. Do I need a loop?
				litserverMsg = literal_eval(serverMsg)
				print(litserverMsg["message"], litserverMsg["speed"])
				#print('Received', repr(data))
					
		except KeyboardInterrupt:
			j.quit()
		except:
			print("Unexpected error:", sys.exc_info()[0])
			break
	s.close()
	j.quit()



except KeyboardInterrupt:
	j.quit()
