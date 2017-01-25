import pygame
#I know there will be other imports for data transmission, but those will be added when this is merged with roy's code

pygame.init()
pygame.event.set_allowed(pygame.JOYAXISMOTION)
stick = pygame.joysick.Joystick(0)
stick.init()
try:
  while true:
    event = pygame.event.wait()
    fb = stick.get_axis(1)
    lr = stick.get_axis(0)
    ud = stick.get_axis(4)
    print ({fb,lr,ud})
except KeyboardInterrupt:
  stick.quit()
  pygame.quit()
