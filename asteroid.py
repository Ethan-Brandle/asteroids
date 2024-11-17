import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		CircleShape.__init__(self, x, y, radius)


		
	def draw(self, screen):
		pygame.draw.circle(screen, "mediumorchid1", self.position, self.radius, width=2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		old_radius = self.radius
		if old_radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			self.random_angle = random.uniform(20, 50)
			new_radius = old_radius - ASTEROID_MIN_RADIUS
			child_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
			child_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
			child_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, self.random_angle) * 1.2
			child_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -self.random_angle) * 1.2
			
			
