class Adafruit_MotorHAT:
  def __init__(self, addr):
    if(addr!=0x60):
      print("Wrong motor address")
    self.motors = {}
    for i in range(1,5):
      self.motors[i]=FakeMotor(i)
  def getMotor(self, idx):
    return self.motors[idx]
  RELEASE = 0
  FORWARD = 1
  REVERSE = -1

class FakeMotor:
  def __init__(self, idx):
    self.idx = idx
    self.running = Adafruit_MotorHAT.RELEASE
    self.speed=0
  def run(self, num):
    self.running = num
  def setSpeed(self, speed):
    self.speed=speed
  def strit(self):
    return `self.idx`+"{"+`self.running`+","+`self.speed`+"}"


