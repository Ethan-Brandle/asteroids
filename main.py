# import libraries
import pygame
from constants import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	# start infinite while loop which will process all game updates
	while True:
		# sets fill color to black 
		screen.fill(000000)
		
		# tells the program to refresh the screen
		pygame.display.flip()
		
		# Check if user has closed window, exit game loop if so
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

if __name__ == "__main__":
	main()
