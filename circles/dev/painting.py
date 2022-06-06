# PAINTING (AGENT) CLASS

import random
from PIL import Image, ImageDraw
from shape import Shape
from hyperparameters import Hyperparameters as hyp

class Painting:
	'''
	METHODS:
		- ability to readout the specs of each shape involved with the painting
		- ability to manipulate the image
			- create the image by generating shapes onto a blank canvas
			- display the painting image to the screen
			- save the painting image to a file
		- ability to perform evolutionary actions onto the painting (agent)
			- cross the agent's genes with another agent's genes to create a child agent
			- mutate the agent's genes to indroduce variability in the agent's evolution

	ATTRIBUTES:
		- the 2D pixel RGB map of a reference image (target)
		- the width and height of a reference image
		- the number of shapes populating each image
		- an array of shape objects representing the object's "genes"
		- an image initialized as a blank canvas
		- an image drawer to populate the canvas with shape objects
		- a tally reperesenting the fitness of the painting object

	NEXT STEPS 05-27-2022
	- remove color mutations, as the color map handles color
	- implement a testing script iterating through all shape placement/mutation combinations
	- after the first batch of tests, include RGBA fitnesses and RGBA mutations while still keeping the colormap configuration and test again
	- document and start working on an application/bot
	'''
	def __init__(self, colormap: list, width: int, height: int, size: int) -> None:
		self.colormap = colormap
		self.width = width
		self.height = height
		self.size = size
		self.genotype = [Shape(colormap = self.colormap,
							   width = self.width, 
							   height = self.height, 
							   factor = 1) for _ in range(0, self.size)]
		#self.create_painting()
		self.fitness = 0

	def __str__(self) -> str:
		'''
		- readout of the specs of each shape populating the agent's canvas
		'''
		return "{}".format(self.genotype)

	def __eq__(self, painting: object) -> bool:
		'''
		- determines if a painting is of the same genetic makeup as another painting
		'''
		return self.genotype == painting.genotype

	def create_painting(self) -> None:
		'''
		- every shape object in the genotype of the painting will be drawn onto the canvas
		'''
		self.sort_genotype(mode = hyp.SORT_GENOTYPE_MODE)
		self.phenotype = Image.new(mode = 'RGB', 
								   size = (self.width, self.height), 
								   color = (255, 255, 255)
		)
		self.draw = ImageDraw.Draw(self.phenotype, 'RGBA')
		for shape in self.genotype: shape.draw_circle(self.draw)

	def sort_genotype(self, mode: str) -> None:
		'''
		| specs:
		| - design in modes to compare methods
		| - extensive documentation!!!
		| - mode #1: larger, more opaque shapes are drawn first
		| - mode #2: smaller, less opaque shapes are drawn first
		| - mode #3: smaller, more opaque shapes are drawn first
		| - mode #4: larger, less opaque shapes are drawn first
		|
		| - mode #5: larger shapes are drawn first
		| - mode #6: smaller shapes are drawn first
		| - mode #7: more opaque shapes are drawn first
		| - mode #8: less opaque shapes are drawn first
		'''
		if mode == '1':
			sort_func = lambda shape: (0.5 * shape.radius) + (0.5 * shape.color[-1])
			self.genotype.sort(reverse = True, key = sort_func)
		elif mode == '2':
			func = lambda shape: (0.5 * shape.radius) + (0.5 * shape.color[-1])
			self.genotype.sort(reverse = False, key = func)
		elif mode == '3':
			max_rad = max([shape.radius for shape in self.genotype])
			sort_func = lambda shape: (0.5 * (max_rad - shape.radius)) + (0.5 * shape.color[-1])
			self.genotype.sort(reverse = True, key = sort_func)
		elif mode == '4':
			max_opac = max([shape.color[-1] for shape in self.genotype])
			sort_func = lambda shape: (0.5 * (max_opac - shape.color[-1])) + (0.5 * shape.radius)
			self.genotype.sort(reverse = True, key = sort_func)
		elif mode == '5':
			self.genotype.sort(reverse = True, key = lambda shape: shape.radius)
		elif mode == '6':
			self.genotype.sort(reverse = False, key = lambda shape: shape.radius)
		elif mode == '7':
			self.genotype.sort(reverse = True, key = lambda shape: shape.color[-1])
		elif mode == '8':
			self.genotype.sort(reverse = False, key = lambda shape: shape.color[-1])
		else:
			'''opt for a random placement of shapes onto the canvas'''
			random.shuffle(self.genotype)

	def show_painting(self) -> None:
		'''
		- displays the populated image onto the screen
		'''
		self.phenotype.show()

	def save_painting(self, painting_id: int) -> None:
		'''
		- saves the populated image as a png file
		'''
		self.phenotype.save('../lib/test_painting{}.png'.format(str(painting_id)))

	def crossover(self, parent_genotype: list, mutation_rate: float) -> object:
		'''
		- agent splits their genes into two parts, 
		  one of which will be combined with another agent's split genes
		- a child painting resulting from crossover and mutation actions will be returned
		- instead of randomly choosing genes to crossover, the image is split in half
		  both horizontally and vertically, such that genes that visibly overlap 
		  will not be altered
		- each combination of split images is considered (00, 01, 10, 11)
		'''
		child = Painting(self.colormap, self.width, self.height, self.size)
		#self.genotype.sort(key = lambda shape: shape.center[0])
		#parent_genotype.sort(key = lambda shape: shape.center[0])
		if random.choice([0, 1]) == 0:
			'''
			- the left half of parent 1 is combined with the right half of parent 2
			'''
			parent1_traits = self.genotype[: int(len(self.genotype) / 2)]
			parent2_traits = parent_genotype[int(len(parent_genotype) / 2) :]
			child.genotype = parent1_traits + parent2_traits
		else:
			'''
			- the right half of parent 1 is combined with the left half of parent 2
			'''
			parent1_traits = self.genotype[int(len(self.genotype) / 2) :]
			parent2_traits = parent_genotype[: int(len(parent_genotype) / 2)]
			child.genotype = parent1_traits + parent2_traits

		child.mutate(mutation_rate, mode = hyp.MUTATION_MODE)
		return child

	def mutate(self, mutation_rate: float, mode: str) -> None:
		'''
		| specs:
		| - design in modes to compare methods
		| - "for" = for shape in shapes...
		| - "if" = if a shape is to be mutated or not
		| - "choose" = choose one of the mutation types
		| - extensive documentation!!!
		'''
		mutation_types = ['shape', 'gene']
		weights = [0.98, 0.02]
		mutation = random.choices(mutation_types, weights = weights, k = 1)[0]
		if mutation == 'shape':
			if mode == '1':
				''' for -> if -> choose'''
				for shape in self.genotype:
					if random.randint(1, int(1 / mutation_rate)) == 1:
						shape_mut_types = ['radius', 'shift']
						shape_weights = [0.50, 0.50]
						'''
						shape_mut_types = ['radius', 'shift', 'R', 'G', 'B', 'A']
						shape_weights = [0.10, 0.10, 0.20, 0.20, 0.20, 0.20]
						'''
						shape_mutation = random.choices(shape_mut_types, 
														weights = shape_weights, 
														k = 1)[0]
						self.choose_mutation(obj = shape, mut_type = shape_mutation)
			elif mode == '2':
				''' for -> choose -> if'''
				for shape in self.genotype:
					shape_mut_types = ['radius', 'shift']
					shape_weights = [0.50, 0.50]
					'''
					shape_mut_types = ['radius', 'shift', 'R', 'G', 'B', 'A']
					shape_weights = [0.10, 0.10, 0.20, 0.20, 0.20, 0.20]
					'''
					shape_mutation = random.choices(shape_mut_types, 
													weights = shape_weights, 
													k = 1)[0]
					if random.randint(1, int(1 / mutation_rate)) == 1:
						self.choose_mutation(obj = shape, mut_type = shape_mutation)
			elif mode == '3':
				''' choose -> for -> if'''
				shape_mut_types = ['radius', 'shift']
				shape_weights = [0.50, 0.50]
				'''
				shape_mut_types = ['radius', 'shift', 'R', 'G', 'B', 'A']
				shape_weights = [0.10, 0.10, 0.20, 0.20, 0.20, 0.20]
				'''
				shape_mutation = random.choices(shape_mut_types, 
												weights = shape_weights, 
												k = 1)[0]
				for shape in self.genotype:
					if random.randint(1, int(1 / mutation_rate)) == 1:
						self.choose_mutation(obj = shape, mut_type = shape_mutation)
			elif mode == '4':
				''' choose -> if -> for'''
				shape_mut_types = ['radius', 'shift']
				shape_weights = [0.50, 0.50]
				'''
				shape_mut_types = ['radius', 'shift', 'R', 'G', 'B', 'A']
				shape_weights = [0.10, 0.10, 0.20, 0.20, 0.20, 0.20]
				'''
				shape_mutation = random.choices(shape_mut_types, 
												weights = shape_weights, 
												k = 1)[0]
				if random.randint(1, int(1 / mutation_rate)) == 1:
					for shape in self.genotype:
						self.choose_mutation(obj = shape, mut_type = shape_mutation)
			elif mode == '5':
				'''if -> choose -> for'''
				if random.randint(1, int(1 / mutation_rate)) == 1:
					shape_mut_types = ['radius', 'shift']
					shape_weights = [0.50, 0.50]
					'''
					shape_mut_types = ['radius', 'shift', 'R', 'G', 'B', 'A']
					shape_weights = [0.10, 0.10, 0.20, 0.20, 0.20, 0.20]
					'''
					shape_mutation = random.choices(shape_mut_types, 
													weights = shape_weights, 
													k = 1)[0]
					for shape in self.genotype:
						self.choose_mutation(obj = shape, mut_type = shape_mutation)
			elif mode == '6':
				''' if -> for -> choose'''
				if random.randint(1, int(1 / mutation_rate)) == 1:
					for shape in self.genotype:
						shape_mut_types = ['radius', 'shift']
						shape_weights = [0.50, 0.50]
						'''
						shape_mut_types = ['radius', 'shift', 'R', 'G', 'B', 'A']
						shape_weights = [0.10, 0.10, 0.20, 0.20, 0.20, 0.20]
						'''
						shape_mutation = random.choices(shape_mut_types, 
														weights = shape_weights, 
														k = 1)[0]
						self.choose_mutation(obj = shape, mut_type = shape_mutation)
			else:
				'''choose a default means of mutation'''
				pass
		else:
			gene_mutation_types = ['add', 'subtract']
			gene_weights = [0.85, 0.15]
			gene_mutation = random.choices(gene_mutation_types, weights = gene_weights, k = 1)[0]
			if gene_mutation == 'add':
				self.genotype.append(self.create_new_gene(factor = 0.5))
			else:
				if self.genotype: self.genotype.pop(0)

	def choose_mutation(self, obj: object, mut_type: str) -> None:
		if mut_type == 'radius': self.mutate_radius(shape = obj)
		elif mut_type == 'shift': self.mutate_coordinates(shape = obj)
		elif mut_type == 'R': self.mutate_color_R(shape = obj)
		elif mut_type == 'G': self.mutate_color_G(shape = obj)
		elif mut_type == 'B': self.mutate_color_B(shape = obj)
		elif mut_type == 'A': self.mutate_color_A(shape = obj)
		else: pass

	def mutate_coordinates(self, shape: object) -> None:
		x_shift = random.randint(-1, 1)
		y_shift = random.randint(-1, 1)
		shape.center = [shape.center[0] + x_shift, shape.center[1] + y_shift]
		shape.center[0] = min(max(shape.center[0], 0), shape.width - 1)
		shape.center[1] = min(max(shape.center[1], 0), shape.height - 1)

	def mutate_color_R(self, shape: object) -> None:
		R_shift = random.randint(-10, 10)
		shape.color[0] = shape.color[0] + R_shift
		shape.color[0] = min(max(shape.color[0], 0), 255)

	def mutate_color_G(self, shape: object) -> None:
		G_shift = random.randint(-10, 10)
		shape.color[1] = shape.color[1] + G_shift
		shape.color[1] = min(max(shape.color[1], 0), 255)

	def mutate_color_B(self, shape: object) -> None:
		B_shift = random.randint(-10, 10)
		shape.color[2] = shape.color[2] + B_shift
		shape.color[2] = min(max(shape.color[2], 0), 255)

	def mutate_color_A(self, shape: object) -> None:
		A_shift = random.randint(-10, 10)
		shape.color[3] = shape.color[3] + A_shift
		shape.color[3] = min(max(shape.color[3], 0), 255)

	def mutate_radius(self, shape: object) -> None:
		shift = random.randint(-1, 1)
		shape.radius = shape.radius + shift

	def mutate_color(self, shape: object) -> None:
		# - mutate opacity
		opacity_shift = random.randint(-30, 30)
		shape.color[-1] += opacity_shift
		shape.color[-1] = min(max(shape.color[-1], 0), 255)

	def create_new_gene(self, factor: float) -> object:
		'''
		- probablistically, an entire new gene will be generated
		'''
		return Shape(self.colormap, self.width, self.height, factor)


if __name__ == "__main__":
	colormap = [[[0,   0,  0], [28,  134, 28], [21,  86,  145]],
				[[255, 34, 0], [128, 255, 0],  [0,   67,  255]],
				[[255, 0,  0], [0,   255, 0],  [255, 255, 255]]]

	painting = Painting(colormap = colormap, width = 3, height = 3, size = 5)
	painting.show_painting()
