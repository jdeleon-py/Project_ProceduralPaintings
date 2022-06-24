# MAIN PROGRAM

import random
from population import Population
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
	population1 = Population(100, 0.10, "../lib/test_target5.png", size = 3)
	generation = 1
	best_fitness = 0
	delta_fit_arr = []

	while True:
		try:
			population1.sort_fitness()
			population1.evaluate_population()

			if population1.population[0].fitness > best_fitness:
				population1.population[0].save_painting('best')
				best_fitness = population1.population[0].fitness

			print("--------------- STATS ---------------")
			print("Generation: {}".format(generation))
			print("Genes Present in Most Fit Organism: {}".format(len(population1.population[0].genotype)))
			print("Population Size: {}".format(len(population1.population)))
			print("Mean Fitness: {}".format(np.mean([i.fitness for i in population1.population])))
			print("Std Fitness: {}".format(np.std([i.fitness for i in population1.population])))
			print("Max Fitness: {}".format(max([i.fitness for i in population1.population])))
			print("Min Fitness: {}".format(min([i.fitness for i in population1.population])))
			print("-------------------------------------")
			generation += 1

			if generation > 50000: break
			
			population1.generate_next_generation()
			population1.adjust_population(generation)
			population1.population[0].save_painting('0')

			if generation % 50 == 0:
				for painting in population1.population:
					painting.genotype.append(painting.create_new_gene(factor = 0.7))

		except KeyboardInterrupt:
			try:
				mean_arr = population1.fit_arr
				gen_arr = np.arange(0, len(mean_arr))

				plt.title("Evolution fitness of the Painting Population")
				plt.xlabel("Generation")
				plt.ylabel("Mean fitness of the population")
				plt.plot(gen_arr, mean_arr)
				plt.show()
				continue
			except KeyboardInterrupt: break
