from Adafruit_MotorHAT import Adafruit_MotorHAT
import atexit
import sys

  # initialize Adafruit motor controll board

motors = []
# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

for i in range(1,5):
	motors.append(mh.getMotor(i))

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	global mh
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)

def setAll(speeds):
	for i in range(0,len(motors)):
		motors[i].setSpeed(speeds[i])

def stopAll():
	for motor in motors:
		motor.setSpeed(0)
# set the speed to start, from 0 (off) to 255 (max speed)


#motors.push(mh.getMotor(3)
#motor2 = mh.getMotor(2)
#motor1 = mh.getMotor(1) #Up and Down Motor