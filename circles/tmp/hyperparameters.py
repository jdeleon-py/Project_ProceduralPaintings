# HYPERPARAMETERS CLASS

class Hyperparameters:
	'''
	- POPULATION SIZE
	- MUTATION RATE
	- SLOW FEEDING GENES OR ALL GENES TOGETHER OPTION
	- TRANSLUCENCY FACTOR
	- MUTATION META-WEIGHTS
	- STARTING NUMBER OF GENES
	- MAXIMUM NUMBER OF GENES
	- TARGET FILE PATH
	- SHAPE TYPE
	- ALLOW ASEXUAL REPRODUCTION OPTION
	- each such hyperparamter will replace various hard-coded coefficients
	  throughout the program, thus making the user variability easier.
	'''
	HYPERPARAMETER = 0

	SORT_GENOTYPE_MODE = 'X'
	MUTATION_MODE = '1'

	GENE_INTEGRATION = True
	STARTING_GENE_NUM = 3
	MAX_GENE_NUM = 500

	MAX_GENERATIONS = 30000

	SHAPE_SIZE_FACTOR = 0.7

	'''
	POPULATION DATA
	- the number of paintings integrated for every generation
	'''
	POPULATION_SIZE = 100

	'''
	AGENT DATA
	- the opaqueness of shapes as they are dependent on the shape's size
	'''
	TRANSLUCENCY_FACTOR = 0.3

	'''
	MUTATIONS
	- the overall probability a mutation will occur
	- the percentage odds a type of mutation will occur
	- all possible types will be listed
	- the collective sum of the probabilities must equal 100
	'''
	MUTATION_RATE = 0.15

	SHAPE_MUTATION_PROB = 0.99
	GENE_MUTATION_PROB = 0.01

	ADD_GENE_PROB = 0.8
	SUBTRACT_GENE_PROB = 0.2

	SHIFT_MUTATION_PROB = 30
	RADIUS_MUTATION_PROB = 30
	COLOR_MUTATION_PROB = 30
	NEW_MUTATION_PROB = 10

	'''
	GENES
	- slow-feeding genes or all genes integrated together option
	- in either case, a maximum number of genes is defined
	- if genes are slowly fed into the pop, then a starting number 
	  of genes is defined
	'''

	'''
	REPRODUCTION
	- allow option for organisms to mate with organisms with identical genes
	'''
	ASEXUAL_REP = True

	'''
	POPULATION INTEGRATION
	- allow for either the most fit half of the population to be preserved
	  for the next generation, or allow for the children to be integrated
	  with any of the population with probablistic determination
	'''
	RANDOM_INT = True

	'''
	FILE
	- a target file path will be defined for
	  grabbing the data of the reference image
	'''
	TARGET_FILE_PATH = "../lib/test_target5.png"


if __name__ == "__main__":
	pass