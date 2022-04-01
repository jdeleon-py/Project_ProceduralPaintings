# IMAGE PROCESSING CLASS

import numpy as np
import imgcompare
from PIL import Image

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
		self.map = self.data.reshape(self.height, self.width, 3) #### this one line could have been the problem area this whole time!!!!!!!!!!

	def get_color_data(self, image):
		'''
		- returns the RGB coordinates of each pixel in the reference image
		- returns a one-dimensional array
		'''
		return np.array(Image.Image.getdata(image))

	def convert_image(self):
		'''
		- some images are in black & white, RGBA, etc...
		- this method normalizes all reference images to be in the RGB format
		'''
		return self.image.convert('RGB')

	def calculate_fitness(self, input_painting):
		'''
		- for each pixel, determine the mean error of the color map
		'''
		input_painting = input_painting.phenotype.convert('RGB')
		diff1_percent = imgcompare.image_diff_percent(self.image, input_painting)
		return 100 - diff1_percent

	def close_image(self):
		'''
		'''
		self.image.close()


if __name__ == "__main__":
	target = Figure('../lib/test_target1.png')

	print('{}'.format(target.map))
	print('{}'.format(target.map.shape))
	'''
	for i in range(0, 30):
		painting = Painting(width = target.width, height = target.height, size = 500)
		fitness = target.calculate_fitness(painting)
		print("Painting Fitness #{0} -> (A generated painting): {1}".format(i + 1, fitness))
	'''