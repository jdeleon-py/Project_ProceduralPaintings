# SHAPE CLASS

import math
import random

class Shape:
	'''
	METHODS:
		- ability to readout the specs of the shape (color, radius, center)
		- ability to define a maximum potential radius as the integer hypotenuse of the width and height
		- ability to draw a circle (ellipse) based on the randomized attributes

	ATTRIBUTES:
		- a predefined width of the image
		- a predefined height of the image
		- a randomized color map (R, G, B, A)
		- a randomized radius value
		- a randomized center coordinate value
		- a deterministic value of the cartesian edge coordinates of the shape [(x0, y0), (x1, y1)]
	'''
	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.R = random.randint(0, 255)
		self.G = random.randint(0, 255)
		self.B = random.randint(0, 255)
		self.A = random.randint(0, 255)
		self.color = (self.R, self.G, self.B, self.A)

		self.radius = random.randint(0, self.get_hypotenuse())
		self.center = (random.randint(0, width), random.randint(0, height))

		self.x0 = self.center[0] - self.radius
		self.x1 = self.center[0] + self.radius
		self.y0 = self.center[1] - self.radius
		self.y1 = self.center[1] + self.radius
		self.coordinates = (self.x0, self.y0, self.x1, self.y1)

	def __str__(self):
		return "Color: {0}; Radius: {1}; Center: {2}".format(self.color, self.radius, self.center)

	def draw_circle(self, drawing_tool):
		drawing_tool.ellipse(self.coordinates, self.color)

	def get_hypotenuse(self):
		return int(math.sqrt((self.width / 3) ** 2 + (self.height / 3) ** 2))

if __name__ == "__main__":
	shape = Shape(width = 800, height = 600)
	print('{}'.format(shape))
