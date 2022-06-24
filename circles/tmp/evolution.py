# EVOLUTION CLASS

import random
import numpy as np
from population import Population
from hyperparameters import Hyperparameters as hyp

class Evolution:
	'''
	- new idea: make the gene editing mechanism a mutation
	- 0.01 chance of adding or subtracting a gene from the agent
	- 80% chance of adding a gene, 20% chance of subtracting a gene

	- test the RGB -> RGBA conversion and how it affects pixel coordinates

	- the 'best' painting may have a lesser amount of genes than the newer paintings
	- along with saving the best painting, save the data of the best painting
		- fitness
		- number of genes
		- etc...

	METHODS:
		-

	ATTRIBUTES:
		-
	'''
	def __init__(self, gene_integration = hyp.GENE_INTEGRATION):
		self.gene_integration = gene_integration
		self.population = Population(hyp.POPULATION_SIZE, 
									 hyp.MUTATION_RATE, 
									 hyp.TARGET_FILE_PATH, 
									 hyp.STARTING_GENE_NUM)
		self.generation = 1
		self.best_fitness = 0

	def evolve(self):
		'''
		'''
		while self.generation < hyp.MAX_GENERATIONS:
			self.population.sort_fitness()
			gene_count = len(self.population.population[0].genotype)
			if gene_count >= hyp.MAX_GENE_NUM: break
			self.population.evaluate_population()
			self.save_best_painting()
			self.display_stats()
			self.population.generate_next_generation()
			self.population.adjust_population(self.generation)
			self.population.population[0].save_painting('_new')
			self.generation += 1

	def save_best_painting(self):
		'''
		'''
		if self.population.population[0].fitness > self.best_fitness:
			self.population.population[0].save_painting('_best')
			self.best_fitness = self.population.population[0].fitness

	def display_stats(self):
		'''
		'''
		print("--------------- STATS ---------------")
		print("Generation: {}".format(self.generation))
		print("Genes Present in Organism: {}".format(len(self.population.population[0].genotype)))
		print("Population Size: {}".format(len(self.population.population)))
		print("Mean Fitness: {}".format(np.mean([i.fitness for i in self.population.population])))
		print("Std Fitness: {}".format(np.std([i.fitness for i in self.population.population])))
		print("Max Fitness: {}".format(max([i.fitness for i in self.population.population])))
		print("Min Fitness: {}".format(min([i.fitness for i in self.population.population])))
		print("-------------------------------------")


if __name__ == "__main__":
	evolver = Evolution()
	evolver.evolve()