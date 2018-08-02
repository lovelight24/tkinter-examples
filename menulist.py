from tkinter import *
from tkinter.filedialog import askopenfilename
from pathlib import Path

class form:
	def __init__(self, root):
		self.menu2 = Menu(root)
		self.parent = root

		new_item= Menu(self.menu2)
		new_item.add_command(label='New', command=self.newwin)
		new_item.add_separator()

		new_item.add_command(label='Open', command=self.openfile)
		new_item.add_separator()

		new_item.add_command(label='Close', command=root.quit)


		self.menu2.add_cascade(label='File', menu=new_item)

		root.config(menu=self.menu2)	
		
	def newwin(self):
		cwin = Toplevel(self.parent)
		cwin.mainloop()


	def openfile(self):
		homedir = str(Path.home())
		fname = askopenfilename(initialdir=homedir, filetypes=(("Text Files: ", "*.txt"), ("All Files: ", "*.*")), title="Choose a file")
		print(fname)
	
		try:
			with open(fname, 'r') as ufile:
				print(ufile.read())
		except Exception as e:
			print(e)


win = Tk()
win.title("Welcome My First Python GUI Project")
a = form(win)
win.mainloop()