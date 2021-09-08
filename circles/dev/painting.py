# PYGAME WINDOW INTERFACE

import pygame
from shape import Shape
from pygame.locals import QUIT

class Painting:
	'''
	METHODS:
	- ability to run a continuous loop throughout the runtime

	ATTRIBUTES:
	- window object to host a display
	- clock object to keep track of a large population of agents
	- list of agents (shape objects) to be drawn onto the display
	- boolean set to indicate whether the program is running
	'''
	MAX_WIDTH = 800
	MAX_HEIGHT = 600

	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Procedural Painting")
		self.window = pygame.display.set_mode([Painting.MAX_WIDTH, Painting.MAX_HEIGHT])
		self.clock = pygame.time.Clock()
		self.shapes = [Shape() for _ in range(0, 100)]
		self.running = True

	def run(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == QUIT: self.running = False

			self.window.fill((255, 255, 255))

			for shape in self.shapes:
				shape.update()
				self.window.blit(shape.surf, shape.rect)

			pygame.display.flip()
			self.clock.tick(30)

	def quit(self):
		pygame.quit()


if __name__ == "__main__":
	painting = Painting()
	painting.run()
	painting.quit()
