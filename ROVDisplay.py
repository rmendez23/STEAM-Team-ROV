import pygame
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND_COLOR = (17, 9, 89)
screen.fill(BACKGROUND_COLOR)
# Set the title of the window
pygame.display.set_caption("STEAM Team ROV Console")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#Set font
font = pygame.font.Font(None, 36)
text = font.render(message, 1, (60,200,40))
textpos = (310,230)


def initGUI(message):
	# Set the width and height of the screen [width, height]
	SCREEN_WIDTH = 800
	SCREEN_HEIGHT = 600
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	BACKGROUND_COLOR = (17, 9, 89)
	screen.fill(BACKGROUND_COLOR)
	# Set the title of the window
	pygame.display.set_caption("STEAM Team ROV Console")
	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()
	#Set font
	font = pygame.font.Font(None, 36)
	text = font.render(message, 1, (60,200,40))
	textpos = (310,230) #text.get_rect(center=(100,100))
	#textpos.centerx = screen.get_rect().centerx
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
		pygame.draw.rect(screen, (60,200,40),(280,200,300,200), 10)
		text = font.render(str(message), 1, (60,100,80))
		screen.blit(text, textpos)
		# --- Update the screen with what we've drawn.
		pygame.display.flip()
		# --- Limit to 60 frames per second
		clock.tick(60)

	# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
