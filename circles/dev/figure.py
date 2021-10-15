# IMAGE COLOR CLASS

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
		self.width, self.height = self.image.size
		self.data = self.get_color_data(self.image)

	def get_color_data(self, image):
		return Image.Image.getdata(image)

	def convert_image(self):
		pass

	def resize_image(self):
		pass

	def close_image(self):
		self.image.close()


if __name__ == "__main__":
	pass
