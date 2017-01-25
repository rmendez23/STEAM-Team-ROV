class Adafruit_MotorHAT:
	def __init__(self, addr):
		if(addr!=0x60):
			print("Wrong motor address")
		self.motors = {}
		for i in range(1,5):
			self.motors[i]=FakeMotor(i)
	def getMotor(self, idx):
		return self.motors[idx]
	RELEASE = 0x1337

class FakeMotor:
	def __init__(self, idx):
		self.idx = idx
		self.speed=0
	def run(self, num):
		print("Running ", num, " on motor ", self.idx)
	def setSpeed(self, speed):
		self.speed=speed
	def strit(self):
		return self.idx+"{"+self.speed+"}"


