# TKINTER APPLICATION CLASS

from tkinter import Tk, Frame, Button, Entry, IntVar
from tkinter.filedialog import asksaveasfile, askopenfile
from painting import Painting

class App:
	'''
	METHODS:
	-

	ATTRIBUTES:
	-
	'''
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.frame.pack()

		self.open_button = Button(self.frame, text = "Open", command = self.open).grid(row = 1, columnspan = 3)
		self.save_button = Button(self.frame, text = "Save", command = self.save).grid(row = 2, columnspan = 3)
		self.display_button = Button(self.frame, text = "Display", command = self.display).grid(row = 3, columnspan = 3)

	def save(self):
		print("Save File!")

	def open(self):
		print("Open File!")

	def display(self):
		print("Display File!")
		painting = Painting()
		painting.run()
		painting.quit()


if __name__ == "__main__":
	root = Tk()
	root.geometry("400x150")
	root.wm_title("Procedural Paintings App (Circles)")
	app = App(root)

	root.mainloop()