# THREAD CLASS

import threading
from figure import Figure

class Thread(threading.Thread):
	'''
	METHODS:
		-

	ATTRIBUTES:
		-
	'''
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = str(threadID)
		self.name = name

	def run(self):


if __name__ == "__main__":
	threadLock = threading.Lock()
	threads = []

