# AGENT CLASS

import random
from painting import Painting

class Agent:
	'''
	METHODS:
		- ability to calculate the fitness of the object's "genotype"
		- ability to display the object's phenotype as the combination of the object's genotype as a string
		- ability to create a new object whose genotype is the split and combined genotypes of the two parent objects
		- ability to change an object's genotype based on a probabilistic outcome

	ATTRIBUTES:
		- an agent will represent a "painting" comprised of n shapes
		- encoded array representing the agent's genotype
		- Ex. [(x, y, z, alpha), (x_cor, y_cor), radius]
		- empty string representing the agent's phenotype
		- integer representing the object's fitness
		- fitness: how accurate a pixel's color is compared to the real image's pixel color
	'''
	MAX_WIDTH = 800
	MAX_HEIGHT = 600

	def __init__(self, size):
		self.size = size
		self.coordinates = [tuple([random.randint(0, MAX_WIDTH), random.randint(0, MAX_HEIGHT)]) for _ in range(0, self.size)]
		self.dimensions = [random.randint(1, MAX_WIDTH) for _ in range(0, self.size)] # radius value for circular shapes
		self.translucency_factor = random.randint(0, 255)
		self.color = [tuple([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]) for _ in range(0, self.size)]
		self.genotype = 0
		self.phenotype = ''
		self.fitness = 0

	def __str__(self):
		return self.genotype

	def calculate_fitness(self, target):
		self.fitness = 0
		target_genotype = [char for char in target]
		for index in range(0, len(self.genotype)):
			if self.genotype[index] == target_genotype[index]:
				self.fitness += 1
		return 2 ** self.fitness

	def crossover(self, parent_genotype, mutation_rate):
		child = Agent(self.size)
		heredity_factor = random.choice([0, 1])
		if heredity_factor == 0:
			child.genotype = parent_genotype[: int(len(parent_genotype) / 2)] + self.genotype[int(len(self.genotype) / 2) :]
		else:
			child.genotype = self.genotype[: int(len(self.genotype) / 2)] + parent_genotype[int(len(parent_genotype) / 2) :]
		child.mutate(mutation_rate)
		return child

	def mutate(self, mutation_rate):
		for index in range(0, len(self.genotype)):
			if random.randint(1, int(1 / mutation_rate)) == 1:
				self.genotype[index] = random.choice(Agent.CORPUS)


if __name__ == "__main__":
	target = "to be or not to be."
	parent1 = Agent(len(target))
	parent2 = Agent(len(target))
	child = parent1.crossover(parent2.genotype, 0.05)

	print("Parent 1: {}".format(parent1))
	print("Fitness of Parent 1: {}".format(parent1.calculate_fitness(target)))
	print('\n')
	print("Parent 2: {}".format(parent2))
	print("Fitness of Parent 2: {}".format(parent2.calculate_fitness(target)))
	print('\n')
	print("Child: {}".format(child))
	print("Fitness of Child: {}".format(child.calculate_fitness(target)))
