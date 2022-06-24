# MUTATION TECHNIQUE/GENE ORDERING GRID SEARCH TEST

from hyperparameters import Hyperparameters as hyp
from evolution import Evolution

if __name__ == "__main__":
	genotype_modes = ['1', '2', '3', '4', '5', '6', '7', '8', 'X']
	mutation_modes = ['1', '2', '3', '4', '5', '6']

	for mut_mode in genotype_modes:
		for gen_mode in genotype_modes:
			hyp.SORT_GENOTYPE_MODE = gen_mode
			hyp.MUTATION_MODE = mut_mode
			evo = Evolution()
			evo.evolve()
