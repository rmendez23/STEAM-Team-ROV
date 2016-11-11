#test_client1.py

#!/usr/bin/python
#Joystick stuff
import serial
import pygame
import time

import socket

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

try:
	#client socket		
	host = socket.gethostname() #change to IP of server   
	port = 12345                   # The same port as used by the server
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object
	s.connect((host, port)) #connect to server
	while (True):
		try:
			pygame.event.pump()
			newSpeed = -250.0*j.get_axis(4)
			print (newSpeed)
			s.sendall(b'Hello, world') #newSpeed in here? s.sendall(newSpeed)
			data = s.recv(1024)
			print('Received', repr(data))
		except KeyboardInterrupt:
			j.quit()
		except Error as err:
			print ("Error in loop:", repr(err))
			j.quit()
	s.close()



except KeyboardInterrupt:
	j.quit()
