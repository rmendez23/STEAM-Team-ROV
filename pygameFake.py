import time

JOYAXISMOTION = 1234

def init():
  print("Pygame Inited")

joy = None

def _Joystick(idx):
  return joy

class Eventer:
  def __init__(self):
    print("event declared")
  def set_allowed(self,code):
    print("Allowing event code", code)
  def wait(self):
    print("waiting for event")
    time.sleep(2)

event = Eventer()

class joystick:
  @staticmethod
  def Joystick(idx):
    return joystick(idx)
  def __init__(self, idx):
    self.idx = idx
  def init(self):
    print("inited joystick with idx ", self.idx)
  def get_axis(self, axis):
    return .5
  def quit(self):
    print("quitting joystick")

def quit():
  print("quitting pygame")
