import socket
from ast import literal_eval

DEBUG = True
host = '127.0.01' if DEBUG else '10.66.66.1'
port = 12345     # Arbitrary non-privileged port
addrTuple = (host, port)

recvBuf = ''

def recvNice(conn):
	global recvBuf
	while (recvBuf.find("\n")<0):
		data = conn.recv(1024)
		if (len(data) == 0):
			raise ValueError("No data recieved - client disconnected")
		#print(("data '"+`len(data)`+"'"))
		recvBuf = recvBuf + str(data)
	idx = recvBuf.find("\n")
	#print("idx "+`idx`+" ; len = "+`len(recvBuf)`)
	ret = recvBuf[:idx]
	recvBuf = recvBuf[(idx+1):]
	return ret
def reprNice(obj):
	return repr(obj)+"\n"
