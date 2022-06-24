# SHAPE CLASS

import math
import random
from hyperparameters import Hyperparameters as hyp

class Shape:
	'''
	METHODS:
		- ability to draw the shape (circle) given a predefined tool
		- ability to define a maximum dimension of the shape's size
		- ability to define colors for shapes based on the shape's center pixel's position
		- ability to define the boundary coordinates for the shape based 
		  on the shape's center and radius
		- ability to readout the shape's specs

	ATTRIBUTES:
		- the 2D pixel RGB map of a reference image (target)
		- the width and height of a reference image
		- a randomly defined radius, with a maximum size being the 
		  hypotenuse of the reference image's dimensions
		- a randomly defined coordinate representing the shape's center
		- a tuple of RGBA values for the shape
	'''
	def __init__(self, colormap, width, height, factor):
		self.colormap = colormap
		self.width = width
		self.height = height
		self.factor = factor
		self.radius = int(0.5 * random.gammavariate(self.factor, 0.1 * self.get_hypotenuse()))
		self.center = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
		self.color = self.define_color()

	def __str__(self):
		'''
		- reads out key specs fo the shape -> (color, center coordinate, radius)
		'''
		return "Color: {0}; Radius: {1}; Center: {2}".format(self.color, self.radius, self.center)

	def define_color(self):
		'''
		- accessing the color map's dimensions to extract each RGB value
		- color is based on the shape's center coordinate
		- transparency values are determined as such:
			- if the shape is larger, then the shape is more transparent
			- larger, more transparent shapes will occupy the background,
			  while smaller, more opaque shapes will occupy the foreground
		'''
		factor = hyp.TRANSLUCENCY_FACTOR * self.get_hypotenuse()
		R = self.colormap[self.center[1]][self.center[0]][0]
		G = self.colormap[self.center[1]][self.center[0]][1]
		B = self.colormap[self.center[1]][self.center[0]][2]
		A = (lambda rad: int((factor - (factor / 255) * rad)))(self.radius)
		return tuple([R, G, B, A])

	def define_drawing_coordinates(self):
		'''
		- the drawing tool requires the shape's boundary coordinates in order to draw
		- the shape's center coordinate and radius are used to compute the boundary points
		'''
		x0 = self.center[0] - self.radius # 180 deg position
		x1 = self.center[0] + self.radius #   0 deg position
		y0 = self.center[1] - self.radius # 270 deg position
		y1 = self.center[1] + self.radius #  90 deg position
		return tuple([x0, y0, x1, y1])

	def draw_circle(self, drawing_tool):
		'''
		- using the PIL library, this function draws an ellipse with symmetrical 
		  coordinates, thus drawing a circle
		- the drawing tool is defined in the Painting object
		'''
		drawing_tool.ellipse(self.define_drawing_coordinates(), self.color)

	def get_hypotenuse(self):
		'''
		- half of the hypotenuse of the width and height dimensions will be the 
		  maximum possible radius defined for a shape
		'''
		return int(math.sqrt((self.width) ** 2 + (self.height) ** 2))


if __name__ == "__main__":
	colormap = [[[0,   0,  0], [28,  134, 28], [21,  86,  145]],
				[[255, 34, 0], [128, 255, 0],  [0,   67,  255]],
				[[255, 0,  0], [0,   255, 0],  [255, 255, 255]]]

	shape = Shape(colormap = colormap, width = 3, height = 3)
	print('{}'.format(shape))
