# import libraries
import pygame
from constants import *
from player import Player

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	# start infinite while loop which will process all game updates
	while True:
		# sets fill color to black 
		screen.fill(000000)
		player.draw(screen)		

		# tells the program to refresh the screen
		player.update(dt)
		pygame.display.flip()
		
		# sets up a tick system for managing the clock
		dt = clock.tick(60) / 1000

		# Check if user has closed window, exit game loop if so
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		

if __name__ == "__main__":
	main()
