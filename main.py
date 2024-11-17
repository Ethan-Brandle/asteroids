# import libraries
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# sprite groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# sprite group assignments
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
	asteroid_field.containers = (updatable)
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	player.containers = (updatable, drawable)
	Shot.containers = (updatable, shots, drawable)




	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	# start infinite while loop which will process all game updates
	while True:
		# sets fill color to black 
		screen.fill((0,0,0))
		asteroid_field

		for obj in updatable:
			obj.update(dt)

		for obj in asteroids:
			for shot in shots:
				if obj.collision(shot):
					obj.split()
					shot.kill()

			if obj.collision(player):
				sys.exit("Game Over!")

		for obj in drawable:
			obj.draw(screen)		

		# tells the program to refresh the screen
		pygame.display.flip()
		
		# sets up a tick system for managing the clock
		dt = clock.tick(60) / 1000

		# Check if user has closed window, exit game loop if so
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		

if __name__ == "__main__":
	main()
