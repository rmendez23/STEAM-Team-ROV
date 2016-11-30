import pygame
import time
import sys

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
#hat_number = j.get_numhats() - 1
print 'Initialized Joystick : %s' % j.get_name()
#print (hat_number)


while True:
	try:
		pygame.event.wait()
		myEvents = pygame.event.get()
		for x in range(0, j.get_numbuttons()-1):
			sys.stdout.write (j.get_button(x) + ",")
			print ("")
	except KeyboardInterrupt:
		j.quit()
