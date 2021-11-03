# AGENT CLASS

import random

class Agent:
	'''

	ATTRIBUTES:
		- an agent will represent a "painting" comprised of n shapes
		- encoded array representing the agent's genotype
		- Ex. [(x, y, z, alpha), (x_cor, y_cor), radius]
		- empty string representing the agent's phenotype
		- integer representing the object's fitness
		- fitness: how accurate a pixel's color is compared to the real image's pixel color
	'''
	def __init__(self):

		self.phenotype = None #Painting(self.size, self.width, self.height)
		self.genotype = [self.color, self.coordinates, self.radius]
		self.fitness = 0

	def calculate_fitness(self, target):
		pass

	def crossover(self, parent_genotype, mutation_rate):
		pass

	def mutate(self, mutation_rate):
		pass


if __name__ == "__main__":
	agent = Agent()
	print('{}'.format(agent))
