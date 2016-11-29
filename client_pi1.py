#test_client1.py

#!/usr/bin/python
#Joystick stuff
import serial
import pygame
import time
import sys

import socket

'''
Gets joystick data and prints it
'''
pygame.init()
#joystick.init()
j = pygame.joystick.Joystick(0)
j.init()
hat_number = j.get_numhats() - 1
print 'Initialized Joystick : %s' % j.get_name()

# Keeps a history of buttons pressed so that one press does
# not send multiple presses to the Arduino Board
button_history = [0,0,0,0,0,0,0,0,0,0,0,0]

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
					newSpeed2 = -250.0*j.get_axis(0)
					s.sendall(repr({"command" : "FB", "speed" : newSpeed1}))
					s.sendall(repr({"command" : "LR", "speed" : newSpeed2}))
					data = s.recv(1024)
					#print('Received', repr(data))
				if e.type == pygame.JOYHATMOTION:
					newSpeed3 = -250.0*j.get_hat(hat_number)[1] #y position tuple of j.get_hat
					s.sendall(repr({"command" : "UD", "speed" : newSpeed3}))
		except KeyboardInterrupt:
			break
		except:
			print("Unexpected error:", sys.exec_info()[0])
			break
	s.close()
	j.quit()



except KeyboardInterrupt:
	j.quit()
