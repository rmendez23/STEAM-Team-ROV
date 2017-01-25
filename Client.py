#client_pi1.py
#!/usr/bin/python
import Common
import time
import sys
from ast import literal_eval
import socket
import time

s = None

#client socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object
s.connect(Common.addrTuple) #connect to server

while (True):
	s.sendall(Common.reprNice( (1,1,1,1) ))
	print("sent")
	time.sleep(1)

