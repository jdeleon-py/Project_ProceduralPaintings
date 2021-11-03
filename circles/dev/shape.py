# SHAPE CLASS

import random

class Shape:
	'''
	METHODS:
		-

	ATTRIBUTES:
		-
	'''
	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.transparency = random.randint(0, 255)
		self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.transparency)

	def draw_circle(self, draw):
		draw.ellipse((x0, y0, x1, y1), self.color)

if __name__ == "__main__":
	pass
