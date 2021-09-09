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

	def _get_fitness(self, agent):
		return agent.calculate_fitness(self.target)


if __name__ == "__main__":
	population = Population(1000, 0.01, "to be or not to be.")
	population.sort_fitness()

	for agent in population.population[:10]:
		print("Fitness: {}".format(agent.fitness))

	print("Most fit genotype: {}".format(population.population[0]))
