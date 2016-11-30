import pygame
import time

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
hat_number = j.get_numhats() - 1
print 'Initialized Joystick : %s' % j.get_name()
print (hat_number)


while True:
	try:
		pygame.event.wait()
		myEvents = pygame.event.get()
		for e in myEvents:
			if e.type == pygame.JOYHATMOTION:
				newSpeed3 = 250.0*j.get_hat(hat_number)[1] #y position tuple of j.get_hat
				print(newSpeed3)
	except KeyboardInterrupt:
		j.quit()
