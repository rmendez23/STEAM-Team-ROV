pygame.init()
pygame.event.set_allowed(pygame.JOYAXISMOTION)
stick = pygame.joysick.Joystick(0)
stick.init()
try:
  while true:
    event = pygame.event.wait()
    fb = stick.get_axis(1)
    lr = stick.get_axis(0)
    motorL = int((fb+lr)*250)
    motorR = int((fb-lr)*250)
    motorV = stick.get_axis(4)
    sendData(0, MotorL)
    sendData(1, MotorR)
    sendData(2, MotorV)
except KeyboardInterrupt:
