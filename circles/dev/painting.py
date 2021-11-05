# PAINTING (AGENT) CLASS

import random
from PIL import Image, ImageDraw
from shape import Shape

class Painting:
	'''
	METHODS:
		- ability to call a shape's draw function to draw a full canvas of shapes
		- ability to display the painting to the screen
		- ability to save the painting as a .png image
		- ability to crossover two parent genotypes onto a child genotype
		- ability to probablisitically change a painting's genotype

	ATTRIBUTES:
		- predefined image width value
		- predefined image height value
		- predefined size value -> determines the number of shapes in a painting
		- genotype list -> an array of shape objects
		- phenotype -> Image object to display
		- fitness value
	'''
	def __init__(self, width, height, size):
		self.width = width
		self.height = height
		self.size = size

		self.genotype = [Shape(self.width, self.height) for _ in range(0, self.size)]
		self.phenotype = Image.new('RGB', (self.width, self.height), (255, 255, 255))
		self.draw = ImageDraw.Draw(self.phenotype, 'RGBA')

		self.create_painting()
		self.fitness = 0

	def __str__(self):
		pass

	def create_painting(self):
		for shape in self.genotype: shape.draw_circle(self.draw)

	def show_painting(self):
		self.phenotype.show()

	def save_painting(self, painting_id):
		self.phenotype.save('../lib/test_painting{}.png'.format(str(painting_id)))

	def crossover(self, parent_genotype, mutation_rate):
		child = Painting(self.width, self.height, self.size)

		child.mutate(mutation_rate)
		return child

	def mutate(self, mutation_rate):
		for shape in self.genotype:
			if random.randint(1, int(1 / (mutation_rate * self.size)) == 1):
				shape = Shape(self.width, self.height)


if __name__ == "__main__":
	painting = Painting(width = 430, height = 430, size = 500)
	painting.show_painting()
	painting.save_painting('0')
