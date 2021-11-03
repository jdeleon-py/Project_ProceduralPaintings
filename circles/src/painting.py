# PAINTING (AGENT) CLASS

import random
import pygame
from pygame.locals import QUIT, KEYDOWN
from shape import Shape

class Painting:
	'''
	METHODS:
		- ability to run a continuous loop throughout the runtime

	ATTRIBUTES:
		- window object to host a display
		- clock object to keep track of a large population of agents
		- list of agents (shape objects) to be drawn onto the display
		- boolean set to indicate whether the program is running
	'''
	def __init__(self, width, height, size):
		pygame.init()
		pygame.display.set_caption("Procedural Painting")

		self.width = width
		self.height = height
		self.size = size

		self.window = pygame.display.set_mode([self.width, self.height])
		self.clock = pygame.time.Clock()

		self.genotype = [Shape(self.width, self.height) for _ in range(0, self.size)]
		self.fitness = 0
		self.running = True

	def crossover(self, parent_genotype, mutation_rate):
		child = Shape(self.width, self.height)

		child.mutate(mutation_rate)
		return child

	def mutate(self, mutation_rate):
		mutation_factor = random.randint(1, int(1 / mutation_rate))
		if mutation_factor == 1:
			print('Mutated!')
			self.transparency = random.randint(0, 255)
			self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.transparency)
			self.coordinates = (random.randint(0, self.width), random.randint(0, self.height))
			self.radius = random.randint(1, int(self.width / 5))
			self.genotype = [self.color, self.coordinates, self.radius]

	def run(self):
		#while self.running:
		for event in pygame.event.get():
			if event.type == QUIT: self.running = False

		self.window.fill((255, 255, 255))

		for shape in self.genotype:
			shape.update()
			self.window.blit(shape.surf, shape.rect)

		pygame.image.save(self.window, "../lib/image.png")

		pygame.display.flip()
		self.clock.tick(30)

	def quit(self):
		pygame.quit()


if __name__ == "__main__":
	painting = Painting(width = 800, height = 600, size = 100)
	painting.run()
	painting.quit()
