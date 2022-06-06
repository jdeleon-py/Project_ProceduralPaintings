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
	'''
	def __init__(self, colormap, width, height, size):
		self.colormap = colormap
		self.width = width
		self.height = height
		self.size = size
		self.shape_factor = 1
		self.genotype = [Shape(self.colormap,
								self.width, 
								self.height, 
								self.shape_factor) for _ in range(0, self.size)]
		self.create_painting()
		self.fitness = 0

	def __str__(self):
		'''
		- readout of the specs of each shape populating the agent's canvas
		'''
		return "{}".format(self.genotype)

	def __eq__(self, painting):
		'''
		- determines if a painting is of the same genetic makeup as another painting
		'''
		return self.genotype == painting.genotype

	def create_painting(self):
		'''
		- every shape object in the genotype of the painting will be drawn onto the canvas
		'''
		self.phenotype = Image.new('RGB', (self.width, self.height), (255, 255, 255))
		self.draw = ImageDraw.Draw(self.phenotype, 'RGBA')
		for shape in self.genotype: shape.draw_circle(self.draw)

	def show_painting(self):
		'''
		- displays the populated image onto the screen
		'''
		self.phenotype.show()

	def save_painting(self, painting_id):
		'''
		- saves the populated image as a png file
		'''
		self.phenotype.save('../lib/test_painting{}.png'.format(str(painting_id)))

	def crossover(self, parent_genotype, mutation_rate):
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

		child.mutate(mutation_rate)
		return child

	def mutate(self, mutation_rate):
		'''
		- the original painting will be copied and mutated by its own probability
		- if the mutated painting has a higher fitness than that of the reference, 
		  then that painting will proceed
		- mutations can be any of the following: 
			- new shape added/ shape removed -> use gamma dist: exp curve
			- shape position and size modified
			- shape transparency modified
		'''
		for shape_index in range(0, len(self.genotype)):
			current_shape = self.genotype[shape_index]
			if random.randint(1, int(1 / mutation_rate)) == 1:
				mutations = ['shift', 'radius', 'color', 'new']
				weights = [hyp.SHIFT_MUTATION_PROB, hyp.RADIUS_MUTATION_PROB, 
							hyp.COLOR_MUTATION_PROB, hyp.NEW_MUTATION_PROB]
				mutation = random.choices(mutations, weights = weights, k = 1)[0]
				if mutation == 'shift': self.mutate_coordinates(current_shape)
				elif mutation == 'radius': self.mutate_radius(current_shape)
				elif mutation == 'color': self.mutate_color(current_shape)
				elif mutation == 'new':
					new_shape = self.create_new_gene(factor = 0.5)
					self.genotype.pop(shape_index)
					self.genotype.append(new_shape)
				else: pass

	def mutate_coordinates(self, shape):
		'''
		- the shape object will shift in place by one pixel probablistically
		- the shape's center will remain inside the frame at all times
		'''
		x_shift = random.randint(-1, 1)
		y_shift = random.randint(-1, 1)
		shape.center = [shape.center[0] + x_shift, shape.center[1] + y_shift]
		shape.center[0] = min(max(shape.center[0], 0), shape.width - 1)
		shape.center[1] = min(max(shape.center[1], 0), shape.height - 1)
		shape.center = tuple(shape.center)
		shape.color = shape.define_color()
		
	def mutate_radius(self, shape):
		'''
		- the shape object will increase or decrease its size by one pixel
		  probablistically
		'''
		shift = random.randint(-1, 1)
		shape.radius = shape.radius + shift
		shape.color = shape.define_color()

	def mutate_color(self, shape):
		'''
		'''
		pass

	def create_new_gene(self, factor):
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
