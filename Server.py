#!/usr/bin/python2.7

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
