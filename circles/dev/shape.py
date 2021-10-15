# SHAPE (AGENT) CLASS

import pygame
import random
from pygame.locals import QUIT

class Shape(pygame.sprite.Sprite):
	'''
	METHODS:
		- ability to draw a circle continuously to the screen
		- ability to calculate the fitness of the object's "genotype"
		- ability to display the object's phenotype as the combination of the object's genotype as a string
		- ability to create a new object whose genotype is the split and combined genotypes of the two parent objects
		- ability to change an object's genotype based on a probabilistic outcome

	ATTRIBUTES:
		- transparency (alpha) value of the shape (randomly generated) 
		- color tuple of the shape (randomly generated) 
		- coordinate tuple of the shape (randomly generated) 
		- dimensions of the shape (randomly generated) 

		- surface object for the shape to be generated onto
		- encoded array representing the agent's genotype
		- Ex. [(x, y, z, alpha), (x_cor, y_cor), radius]
	'''
	def __init__(self, width, height):
		pygame.sprite.Sprite.__init__(self)

		self.width = width
		self.height = height

		self.transparency = random.randint(0, 255)
		self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.transparency)
		self.coordinates = (random.randint(0, self.width), random.randint(0, self.height))
		self.radius = random.randint(1, self.width)

		self.surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
		self.rect = self.surf.get_rect()

		self.genotype = [self.color, self.coordinates, self.radius]
		self.fitness = 0

	def __str__(self):
		return "Genotype: {}".format(self.genotype)

	def update(self):
		pygame.draw.circle(self.surf, self.color, self.coordinates, self.radius)

	def calculate_fitness(self, target):
		pass

	def crossover(self, parent_genotype, mutation_rate):
		pass

	def mutate(self, mutation_rate):
		pass


if __name__ == "__main__":
	shape1 = Shape()
	shape2 = Shape()

	print("Shape 1: {}".format(shape1.genotype))
	print("Shape 2: {}".format(shape2.genotype))

	pygame.init()
	pygame.display.set_caption("Shape Test")
	window = pygame.display.set_mode([shape1.width, shape1.height])
	clock = pygame.time.Clock()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == QUIT: running = False
		window.fill((255, 255, 255))

		shape1.update()
		window.blit(shape1.surf, shape1.rect)
		shape2.update()
		window.blit(shape2.surf, shape2.rect)

		pygame.display.flip()
		clock.tick(30)

	pygame.quit()
