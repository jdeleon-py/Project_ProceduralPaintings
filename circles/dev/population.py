# POPULATION CLASS

import random
from figure import Figure
from painting import Painting
from hyperparameters import Hyperparameters as hyp

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
		- the probabilistic rate at which a mutation can occur within a painting object
		- target encoded array that the agents should strive for
		- the size of the target
		- array of children agent objects
	'''
	def __init__(self, max_population, mutation_rate, target_path, size):
		self.max_population = max_population
		self.mutation_rate = mutation_rate
		self.target_path = target_path
		self.size = size
		self.target = Figure(self.target_path)
		self.population = [Painting(self.target.map, 
									self.target.width, 
									self.target.height, 
									self.size) for _ in range(0, self.max_population)]
		self.children = []
		self.fit_arr = []

	def choose_parent(self):
		'''
		- probablistically chooses an agent based on the agent's fitness score
		- more fit organisms are more likely to be chosen as parents
		'''
		weights = [painting.fitness for painting in self.population]
		return random.choices(self.population, weights = weights, k = 1)[0]

	def evaluate_population(self):
		'''
		- every painting object generates an image based on its hyperparameters
		  and thus, determines the fitness of the population
		- fitnesses are sorted in descending order, with the most fit organism first
		- the mean fitness of the population is recorded for analysis
		'''
		for painting in self.population: 
			painting.create_painting()
			painting.fitness = self.target.calculate_fitness(painting)
		mean = self.calculate_mean_fitness()
		self.fit_arr.append(mean)
		self.sort_fitness()

	def generate_next_generation(self, asexual = hyp.ASEXUAL_REP):
		'''
		- for a number of iterations half of that of the population
		- children painting objects are generated
			- option can be made to choose identical or non-identical parents
		- children organisms have half/half genes from both parents
		- a children array is accumulated with half the size of the population
		'''
		self.children = []
		self.scale_fitness()
		for _ in range(0, len(self.population), 2):
			if asexual == True:
				'''
				- possibility of both parents being identical organisms
				- (asexual reproduction)
				'''
				parent1 = self.choose_parent()
				parent2 = self.choose_parent()
			else:
				'''
				- organisms in the population must be unique in order to mate
				- (sexual reproduction)
				'''
				parent1 = self.choose_parent()
				parent2 = self.choose_parent()
				while parent1 == parent2: parent2 = self.choose_parent()
			child = parent1.crossover(parent2.genotype, self.mutation_rate)
			self.children.append(child)

	def adjust_population(self, gen, random_integration = hyp.RANDOM_INT):
		'''
		- integrate the children organisms into the population
		- an option for integration to produce a new population:
			- pair the children with the most fit half of the original 
			  population
			- at random moments, to encourage variability among the 
			  evolutionary process, pair the children with half of the 
			  original population of any probablisitic fitness
			  (more fit organisms are more likely to be put back into the population)
		'''
		if random_integration == True:
			self.sort_fitness()
			marker = 0
			if gen % marker == 0:
				weights = [painting.fitness for painting in self.population]
				self.population = self.sample(weights, k = int(0.5 * self.max_population)) + self.children
			else:
				self.population = self.population[: int(len(self.population) / 2)] + self.children
		else:
			self.population = self.population[: int(len(self.population) / 2)] + self.children

	def sample(self, weights, k):
		'''
		- helper function to sample an array returning unique elements
		- applied to population to return a new population half the size
		- new population favors higher fitnesses and is combined with
		  the children population to produce the overall population for
		  the next generation
		'''
		weighted_arr = list(weights)
		population_indices = range(len(self.population))
		sample_indices = []
		while True:
			remaining = k - len(sample_indices)
			if not remaining: break
			for i in random.choices(population_indices, weights = weighted_arr, k = remaining):
				if weighted_arr[i]:
					weighted_arr[i] = 0.0
					sample_indices.append(i)
		return [self.population[i] for i in sample_indices]

	def sort_fitness(self):
		'''
		- organisms in the population are sorted by fitness
		- the most fit organism is the first index of the sorted population
		'''
		self.population.sort(reverse = True, key = lambda painting: painting.fitness)

	def scale_fitness(self):
		'''
		- organisms with higher fitnesses are emphasized
		- to encourage a swift evolution, in a space of organisms with high fitnesses,
		  more distinct organisms with higher fitnesses are more likely to be chosen
		'''
		self.sort_fitness()
		for i in range(0, len(self.population)):
			self.population[i].fitness = int(10 * (self.max_population / ((i + 1) ** 0.5)))

	def calculate_mean_fitness(self):
		'''
		'''
		fitness_arr = [painting.fitness for painting in self.population]
		return sum(fitness_arr) / len(fitness_arr)


if __name__ == "__main__":
	population = Population(10, 0.01, "../lib/test_target0.png", size = 500)
	population.sort_fitness()

	for agent in population.population[:10]:
		print("Fitness: {}".format(agent.fitness))

	#print("Most fit genotype: {}".format(population.population[0]))
