# IMAGE PROCESSING CLASS

import numpy as np
from PIL import Image

# For testing:
'''
from painting import Painting
'''

class Figure:
	'''
	METHODS:
		- ability to process the image into a numpy array of color maps
		- ability to convert an incoming image into an 'RGB' configuration
		- ability to calculate the fitness between the target and input painting:
		- ability to close the image object after usage

	ATTRIBUTES:
		- a predefined value representing the path of the image
		- an image object opening an existing image
		- a width and height value, of which determines all shape and painting width/height
		- an array of the image object's color map per pixel
	'''
	def __init__(self, path):
		self.path = path
		self.image = Image.open(self.path)
		self.image = self.convert_image()
		self.width, self.height = self.image.size
		self.data = self.get_color_data(self.image)

	def get_color_data(self, image):
		return np.array(Image.Image.getdata(image))

	def convert_image(self):
		return self.image.convert('RGB')

	def calculate_fitness(self, input_painting):
		'''
		- for each pixel, determine the mean error of the color map
		'''
		fitness = 255 - np.abs(input_painting - self.data)
		fitness = fitness.sum(axis = 1) / 3
		return fitness.mean()

	def close_image(self):
		self.image.close()


if __name__ == "__main__":
	target = Figure('../lib/test_target.png')
	painting = Painting(width = target.width, height = target.height, size = 500)
	painting.save_painting('0')

	painting_image1 = Figure('../lib/test_painting0.png')
	fitness1 = target.calculate_fitness(painting_image1.data)

	painting_image2 = Figure('../lib/test_target.png')
	fitness2 = target.calculate_fitness(painting_image2.data)

	print("Painting Fitness #1 -> (A generated painting):          {}".format(fitness1))
	print("Painting Fitness #2 -> (A replica of the target image): {}".format(fitness2))
