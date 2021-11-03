# IMAGE COLOR CLASS

import numpy as np
from PIL import Image

class Figure:
	'''
	METHODS:
		- ability to grab and store an image's pixel colors
		- ability to convert images between RGB scale and RGBA scale
		- ability to resize the image

	ATTRIBUTES:
		- path string to target image
		- PIL image object of target image
		- list of target image pixel colors
	'''
	def __init__(self, path):
		self.path = path
		self.image = Image.open(self.path)
		self.greyscale_image = self.convert_image()
		self.width, self.height = self.image.size
		self.data = self.get_color_data(self.image)
		self.greyscale_data = self.get_color_data(self.greyscale_image)

	def get_color_data(self, image):
		return Image.Image.getdata(image)

	def convert_image(self):
		return self.image.convert('L')

	def resize_image(self):
		pass

	def close_image(self):
		self.image.close()


if __name__ == "__main__":
	pass
