from tkinter import *
from tkinter.filedialog import askopenfilename
from pathlib import Path

class form:
	def __init__(self, root):
		self.texte1 = ""
		self.texte2 = ""
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

		# Create Canvas
		C = Canvas(root, bg="blue", height=250, width=300)
		C.pack(expand=True, fill=BOTH)

		# Add Background Image in Canvas
		mainbgimg = PhotoImage(file = "images\\main-bg.gif", width=300, height=250)
		C.img = mainbgimg
		C.create_image(0,0, anchor=NW, image=mainbgimg) 
		
		


	def show_entry_value(self):
		print(self.texte1.get())
#		print("name is %s and mobile is %s" %(self.texte1.get(), self.texte2.get()))		



	def newwin(self):
		cwin = Toplevel(self.parent)
		
		Label(cwin, text="Name: ").grid(row=0)
		Label(cwin, text="mobile: ").grid(row=1)
		
		Entry(cwin, textvariable=self.texte1).grid(row=0, column=1)
		Entry(cwin, textvariable=self.texte2).grid(row=1, column=1)

		Button(cwin, text="Quit", command=cwin.destroy).grid(row=2)
		Button(cwin, text="Submit", command=self.show_entry_value).grid(row=2, column=1)

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