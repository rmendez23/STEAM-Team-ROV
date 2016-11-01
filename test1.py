#!/usr/bin/python

import serial
import pygame
import time

try:
	while (True):
		pygame.event.pump()
		newSpeed = -250.0*j.get_axis(4)
		print (newSpeed)
