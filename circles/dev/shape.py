# SHAPE CLASS

import random
import pygame

MAX_WIDTH = 800
MAX_HEIGHT = 600

class Shape(pygame.sprite.Sprite):
	'''
	METHODS:
	- ability to draw a circle continuously to the screen

	ATTRIBUTES:
	- transparency (alpha) value of the shape (randomly generated)
	- color tuple of the shape (randomly generated)
	- coordinate tuple of the shape (randomly generated)
	- dimensions of the shape (randomly generated)

	- surface object for the shape to be generated onto
	'''
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.transparency = random.randint(0, 255)
		self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.transparency)
		self.coordinates = (random.randint(0, MAX_WIDTH), random.randint(0, MAX_HEIGHT))
		self.radius = random.randint(1, MAX_WIDTH)

		self.surf = pygame.Surface((MAX_WIDTH, MAX_HEIGHT), pygame.SRCALPHA)
		self.rect = self.surf.get_rect()

	def update(self):
		pygame.draw.circle(self.surf, self.color, self.coordinates, self.radius)


if __name__ == "__main__":
	pygame.init()
	pygame.display.set_caption("Shape Test")
	window = pygame.display.set_mode([MAX_WIDTH, MAX_HEIGHT])
	clock = pygame.time.Clock()

	shape1 = Shape()
	shape2 = Shape()

	running = True
	while running:
		window.fill((255, 255, 255))

		shape1.update()
		window.blit(shape1.surf, shape1.rect)
		shape2.update()
		window.blit(shape2.surf, shape2.rect)

		pygame.display.flip()
		clock.tick(30)

	pygame.quit()
