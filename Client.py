#!/usr/bin/python2.7
import Common
import time
import sys
from ast import literal_eval
import socket
import time
if Common.DEBUG:
  import pygameFake as pygame
else:
  import pygame

#client socket, connects to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object
s.connect(Common.addrTuple) #connect to server

def sendObject(obj):
  global s
  s.sendall( Common.reprNice(obj) )

pygame.init()
pygame.event.set_allowed(pygame.JOYAXISMOTION)
stick = pygame.joystick.Joystick(0)
stick.init()

try:
  while True:
    event = pygame.event.wait()
    fb = stick.get_axis(1)
    lr = stick.get_axis(0)
    motorL = int((-fb+lr)*250)
    motorR = int((-fb-lr)*250)
    motorV = stick.get_axis(4)*250
    sendObject( (motorL, motorR, motorV, 0) )
except KeyboardInterrupt:
  stick.quit()
  pygame.quit()

