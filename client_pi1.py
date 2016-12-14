#client_pi1.py
#!/usr/bin/python
import serial
import pygame
import time
import sys
from ast import literal_eval
import socket
import ROVDisplay #for the GUI

'''
Gets joystick data and prints it
'''
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
print 'Initialized Joystick : %s' % j.get_name()

recvBuf = ''
def recvNice(s):
	global recvBuf
	idx = recvBuf.find("\n")
	print("idx "+`idx`+" ; len = "+`len(recvBuf)`)
	if idx<1:
		data = s.recv(1024) #s.recv(1024)?
		#print("data '"+data+"'")
		recvBuf = recvBuf + data
		return recvNice(s)
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
					upSpeed = 250.0*j.get_button(3) #button 
					downSpeed = 250.0*j.get_button(0) #down button
					s.sendall(reprNice({"command" : "U", "speed" : upSpeed}))
					s.sendall(reprNice({"command" : "D", "speed" : downSpeed}))
					
				'''
				serverMsg = recvNice(s) #Not sure if I did this right. Do I need a loop?
				litserverMsg = literal_eval(serverMsg)
				print(litserverMsg["message"], litserverMsg["speed"])
				initGUI(litserverMsg["message"])
				'''
					
		except KeyboardInterrupt:
			j.quit()
		except:
			print("Unexpected error:", sys.exc_info()[0])
			break
	s.close()
	j.quit()



except KeyboardInterrupt:
	j.quit()
