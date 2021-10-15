# PAINTING (POPULATION) CLASS

import math
import pygame
from pygame.locals import QUIT, KEYDOWN
from shape import Shape
from figure import Figure

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
	def __init__(self, max_population, mutation_rate):
		pygame.init()
		pygame.display.set_caption("Procedural Painting")

		self.max_population = max_population
		self.mutation_rate = mutation_rate
		self.image = Figure(path = '../lib/img.jpg')
		self.target = self.image.data
		self.target_size = len(self.target)

		self.window = pygame.display.set_mode([self.image.width, self.image.height])
		self.clock = pygame.time.Clock()

		self.population = [Shape(self.image.width, self.image.height) for _ in range(0, self.max_population)]
		self.children = []
		self.running = True

	def choose_parent(self, weight):
		return random.choices(self.population, weights = weight, k = 1)[0]

	def generate_next_generation(self):
		self.children = []
		weights = [self.calculate_fitness(agent) for agent in self.population]

		for _ in range(0, len(self.population), 2):
			parent1 = self.choose_parent(weights)
			parent2 = self.choose_parent(weights)
			child = parent1.crossover(parent2.genotype, self.mutation_rate)
			self.children.append(child)

	def adjust_population(self):
		self.population = self.population[: int(len(self.population) / 2)] + self.children

	def compare_agent(self):
		self.sort_fitness()
		return self.population[0].__str__() == self.target

	def sort_fitness(self):
		self.population.sort(reverse = True, key = self._get_fitness)

	def calculate_fitness(self, agent):
		'''
		- compare pixel colors of target image to those of generated image
		- if a pixel color is desirable, all shapes involved get a fitness point
		- if for each shape: if radius < dist(x1, y1, x2, y2): pixel is within range
		'''
		gen_image = Figure(path = '../lib/image.png')
		agent.fitness = 0
		for i in range(0, self.target_size):
			color_compare = self.compare_color(self.target[i], gen_image.data[i])
			target_coor = self.get_coordinates(self.target[i])
			pixel_dist = self.get_distance(target_coor, agent.coordinates)
			if color_compare and (pixel_dist <= agent.radius):
				agent.fitness += 1
		return agent.fitness

	def get_distance(self, target_coor, shape_coor):
		return math.sqrt(((shape_coor[0] - target_coor[0]) ** 2) + ((shape_coor[1] - target_coor[1]) ** 2))

	def get_coordinates(self, image_index):
		pass

	def compare_color(self, target_index, figure_index):
		pass

	def get_midpoint(self, x1, x2, y1, y2):
		return tuple([0.5 * (x1 + x2), 0.5 * (y1 + y2)])

	def run(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == QUIT: self.running = False
				if event.type == KEYDOWN: pygame.image.save(self.window, "../lib/image.png")

			self.window.fill((255, 255, 255))

			for shape in self.population:
				shape.update()
				self.window.blit(shape.surf, shape.rect)

			pygame.display.flip()
			self.clock.tick(30)

	def quit(self):
		pygame.quit()


if __name__ == "__main__":
	painting = Painting(max_population = 300, mutation_rate = 0.2)
	painting.run()
	painting.quit()
