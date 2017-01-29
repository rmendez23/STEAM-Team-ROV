import Common
import atexit
import sys

if Common.DEBUG:
  from Adafruit_MotorHATFake import Adafruit_MotorHAT
else:
  from Adafruit_MotorHAT import Adafruit_MotorHAT

  # initialize Adafruit motor controll board
motors = []
# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)
for i in range(1,5):
  motors.append(mh.getMotor(i))

  # recommended for auto-disabling motors on shutdown
def turnOffMotors():
  global mh
  mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)

  # takes a motor and a speed (-255,255) and sets the correct direction and speed
def setMotorSpeed(motor, speed):
  absSpeed = speed if speed>=0 else 0-speed
  if speed==0:
    motor.run(Adafruit_MotorHAT.RELEASE)
  elif speed>0:
    motor.run(Adafruit_MotorHAT.FORWARD)
  else:
    motor.run(Adafruit_MotorHAT.REVERSE)
  motor.setSpeed(absSpeed)

def strit():
  ret = ""
  for motor in motors:
    ret=ret+motor.strit()+","
  return ret

def setAll(speeds):
  for i in range(0,len(motors)):
    setMotorSpeed(motors[i], speeds[i])
  print("set motors to ", strit())

def stopAll():
  for motor in motors:
    setMotorSpeed(motor, 0)

# speeds are from 0 (off) to 255 (max speed)
# direction is set with motor.run(<direction>) wheren <direction> is one of Adafruit_MotorHAT.{RELEASE,FORWARD,REVERSE}
