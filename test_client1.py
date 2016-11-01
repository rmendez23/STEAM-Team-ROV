#!/usr/bin/python
#Joystick stuff
import serial
import pygame
import time

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
	while (True):
		pygame.event.pump()
		newSpeed = -250.0*j.get_axis(4)
		print (newSpeed)
