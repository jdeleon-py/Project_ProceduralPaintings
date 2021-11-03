# POPULATION CLASS

import random
from agent import Agent

class Population:
	'''
	METHODS:
		- ability to create a mating pool based on the most fit agent objects
		- ability to breed the next generation of agent objects
		- ability to adjust the population by including the most fit parents and the children
		- ability to compare the target str to the most fit agent
		- ability to sort the agent objects based on fitness
		- ability to return the fitness of the agent object

	ATTRIBUTES:
		- array of agent objects with max population parameter
		- mutation rate 
		- target encoded array that the agents should strive for
		- the size of the target
		- array of children agent objects
	'''
	def __init__(self, max_population, mutation_rate, target):
		self.max_population = max_population
		self.mutation_rate = mutation_rate
		self.target = target
		self.target_size = len(self.target)

		self.population = [Agent(self.target_size) for _ in range(0, self.max_population)]
		self.children = []

	def choose_parent(self, weight):
		return random.choices(self.population, weights = weight, k = 1)[0]

	def generate_next_generation(self):
		self.children = []
		weights = [self._get_fitness(agent) for agent in self.population]

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
			grey_pix = self.get_grey_pixel(agent.genotype[0])
			color_fit_agent = self.compare_color(self.image.greyscale_data[i], grey_pix)
			color_fit_image = self.compare_color(self.image.greyscale_data[i], gen_image.greyscale_data[i])
			target_coor = self.get_coordinates(i)
			pixel_dist = self.get_distance(target_coor, agent.genotype[1])
			if (pixel_dist <= agent.genotype[2]):
				agent.fitness += color_fit_agent
				agent.fitness += color_fit_image
		return agent.fitness

	def get_distance(self, target_coor, shape_coor):
		return int(math.sqrt(((shape_coor[0] - target_coor[0]) ** 2) + ((shape_coor[1] - target_coor[1]) ** 2)))

	def get_grey_pixel(self, color):
		#return (color[0] + color[1] + color[2] + (3 * color[3])) / 4
		return (color[0] * 0.299) + (color[1] * 0.587) + (color[2] * 0.114)

	def get_coordinates(self, image_index):
		return tuple([image_index % self.image.width, int(image_index / self.image.width)])

	def compare_color(self, target_index, agent_index):
		'''
		- compares a generated pixel's color to the target pixel's color
		- returns a True or False if any of the RGB values are within a desirable range
		- let a desirable pixel have a specified degrees of freedom
		'''
		r_diff = (target_index - agent_index)
		g_diff = (target_index - agent_index)
		b_diff = (target_index - agent_index)
		color_diff = math.sqrt((r_diff ** 2) + (g_diff ** 2) + (b_diff ** 2))
		return 255 - int(color_diff)
		'''
		r_fitness = abs(agent_index[0] - target_index[0])
		g_fitness = abs(agent_index[1] - target_index[1])
		b_fitness = abs(agent_index[2] - target_index[2])
		return int((r_fitness + g_fitness + b_fitness) / 255)
		'''

	def calculate_accuracy(self):
		fitness = 0
		target_fitness = 3 * self.image.width * self.image.height
		for agent in self.population: fitness += agent.fitness
		return 100 * (fitness / target_fitness)


if __name__ == "__main__":
	population = Population(1000, 0.01, "to be or not to be.")
	population.sort_fitness()

	for agent in population.population[:10]:
		print("Fitness: {}".format(agent.fitness))

	print("Most fit genotype: {}".format(population.population[0]))
