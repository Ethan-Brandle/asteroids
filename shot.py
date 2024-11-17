import pygame
import random
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
	def __init__(self, x, y, radius):
		CircleShape.__init__(self, x, y, radius)
		
	def draw(self, screen):
		pygame.draw.circle(screen, "indianred1", self.position, SHOT_RADIUS, width=2)


	def update(self, dt):
		self.position += self.velocity * dt