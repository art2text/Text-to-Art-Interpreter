# main.py: Creates the GUI for the Text-to-Art Application.
# Wallis Muraca
# Nov 27,2017 
# 
# Skeleton Tk interface example
# Written by Bruce Maxwell
# Modified by Stephanie Taylor

# standard library dependencies

try:
    import tkinter as tk
    import tkinter.font as tkf
    import tkinter.simpledialog as tks
    from tkinter import StringVar
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk 
    import tkFont as tkf
    import tkFileDialog as tks
    from Tkinter import StringVar
    import tkFileDialog as filedialog
import turtle as t
import os


import turtle as t
import os

# our custom classes
import Parser as parser 
import Drawer as drawer
import DataStorage as storage

class DisplayApp:
	""" DisplayApp class for Text-to-Art Interpreter to put everything together. """
	
	'''
	initialize the DisplayApp instance
	'''
	def __init__(self, width, height):

		# create a tk object, which is the root window
		self.root = tk.Tk()

		# width and height of the window
		self.initDx = width
		self.initDy = height

		# set up the geometry for the window
		self.root.geometry( "%dx%d+50+30" % (self.initDx, self.initDy) )
	
		# our text file parser
		self.parser = None
		
		# our drawer to create images in the canvas
		self.drawer = None
		
		# data storage object to record past drawings
		self.storage = storage.DataStorage()
		
		# whether a turtle has been created yet
		self.createdTurtle = False

		# set the title of the window
		self.root.title("Text-to-Art Interpreter")

		# set the maximum size of the window for resizing
		self.root.maxsize( 1600, 900 )

		# Filename List, to keep track of which text files have been read in
		self.filenameList = []

		# build the controls
		self.buildControls()

		# build the Canvas
		self.buildCanvas()

		# bring the window to the front
		self.root.lift()

		# - do idle events here to get actual canvas size
		self.root.update_idletasks()

		# set up the key bindings
		self.setBindings()

	'''	
	create the canvas object
	
	@return None
	'''
	def buildCanvas(self):
		self.canvas = tk.Canvas( self.root, width=self.initDx, height=self.initDy )
		self.canvas.pack( expand=tk.YES, fill=tk.BOTH )
	
	'''
	build a frame and create user GUI controls such as buttons 
	
	@return None
	'''
	def buildControls(self):

		# make a control frame on the right for user interaction
		rightcntlframe = tk.Frame(self.root)
		rightcntlframe.pack(side=tk.RIGHT, padx=2, pady=2, fill=tk.Y)


		# make a separator frame
		sep = tk.Frame( self.root, height=self.initDy, width=2, bd=1, relief=tk.SUNKEN )
		sep.pack( side=tk.RIGHT, padx = 2, pady = 2, fill=tk.Y)

		# use a label to set the size of the right panel
		label = tk.Label( rightcntlframe, text="Previous Drawings:", width=20 )
		label.pack( side=tk.TOP, pady=10 )
		
		# create the GUI list of read in text files
		self.filesBox = tk.Listbox(rightcntlframe, selectmode=tk.SINGLE, exportselection=0, height=7)
		self.filesBox.pack(side=tk.TOP)
		self.filesBox.pack(fill=tk.X)
		# get previous drawings from storage
		previousDrawings = self.storage.getData()
		for drawing in previousDrawings:
			self.filenameList.append(drawing[1])
			self.filesBox.insert(len(self.filenameList),drawing[0])


		# make a ope file button in the frame.
		button = tk.Button( rightcntlframe, text="Open New Text File", 
							   command=self.handleOpen )
		button.pack(side=tk.TOP, pady = 3)  # default side is top

		# make the draw button
		button = tk.Button( rightcntlframe, text="Draw Picture of Text File", 
							   command=self.createDrawing)
		button.pack(side=tk.TOP)  # default side is top
		
		# make erase drawing button
		button = tk.Button( rightcntlframe, text="Erase Picture", 
							   command=self.clearCanvas )
		button.pack(side=tk.TOP, pady = 20)  # default side is top
	
	'''
	bind keyboard shortcuts to functionality in the app
	
	@return None
	'''
	def setBindings(self):

		# bind command sequences to the root window
		#### Quit and clear buttons, respectively ####
		self.root.bind( '<Command-q>', self.handleQuit )
		self.root.bind( '<Command-n>', self.clearCanvas )

	'''
	handles when a user quits
	
	@return None
	'''
	def handleQuit(self, event=None):
		print ('Terminating')
		self.root.destroy()
	
	'''
	creates an instance of a turtle and place it in the drawing canvas
	
	@return None
	'''	
	def makeTurtle(self):
		self.turt = t.RawTurtle(self.canvas)
		self.turt.hideturtle()
		screen = self.turt.getscreen()
		screen.bgcolor("white")
		self.createdTurtle = True
		
	
	''' @OldVersion
	def makeTurtle(self):
		self.turt = t.RawTurtle(self.canvas)
		screen = self.turt.getscreen()
	'''
	

	'''
	create the drawing in the canvas
	
	@param reducedWidth (int), amount of x-axis canvas space to limit from turtle to ensure padding
	@param reducedHeight (int), amount of y-axis canvas space to limit from turtle to ensure padding
	@return None
	'''
	def createDrawing(self, reducedWidth = 500, reducedHeight = 200):
		# get list of chars from selected file and store in object field
		if len(self.filesBox.curselection()) is 0:
			print("Please upload or select a file first")
			return
		selectedFileNumber = self.filesBox.curselection()[0]
		characters = self.filenameList[selectedFileNumber]
		self.characterList = characters
		
		# create turtle if needed, else clear canvas
		if not self.createdTurtle:
			self.makeTurtle()
		else:
			self.clearCanvas()
			
		# draw picture and update canvas	
		self.turt.getscreen().tracer(0)
		self.drawer = drawer.Drawer(self.characterList, self.turt, self.initDx - reducedWidth, self.initDy - reducedHeight)
		self.drawer.draw()
		self.turt.getscreen().update()
		
		
	''' @OldVersion
	def createDrawing(self, reducedWidth = 500, reducedHeight = 200):
		# get list of chars from selected file and store in object field
		selectedFileNumber = self.filesBox.curselection()[0]
		characters = self.filenameList[selectedFileNumber]
		self.characterList = characters
		
		# draw picture and update canvas	
		self.drawer = drawer.Drawer(self.characterList, self.turt, self.initDx - reducedWidth, self.initDy - reducedHeight)
		self.drawer.draw()
	'''
	
	'''
	handles when a new file is being read in
	
	@param event (function), event which triggers this method
	@return None
	'''
	def handleOpen(self, event=None):
		# allow user to browse for new file
		fn = filedialog.askopenfilename(parent=self.root,title="Choose file", initialdir='.')
		
		# clear all previously highlighted file suggestions
		self.filesBox.selection_clear(0, tk.END)

		if fn is not '':
			# parse new file and get representative list of chars
			self.parser = parser.Parser(fn)
			self.characterList = self.parser.get_characters_list()
			
			# save file into our GUI list of files and our external storage if a text file
			base = os.path.basename(fn)
			if base.endswith('.txt'):
				self.storage.saveData(self.characterList, base)
				self.filenameList.append(self.characterList)
				self.filesBox.insert(len(self.filenameList),base)
				self.filesBox.pack(fill=tk.X)
				self.filesBox.select_set(len(self.filenameList) - 1)
		
			
	''' @OldVersion
	def handleOpen(self, event=None):
		# allow user to browse for new file
		fn = filedialog.askopenfilename(parent=self.root,title="Choose file", initialdir='.')

		# parse new file and get representative list of chars
		self.parser = parser.Parser(fn)
		self.characterList = self.parser.get_characters_list()
		
		# save file into our GUI list of files
		base = os.path.basename(fn)
		self.filenameList.append(self.characterList)
		self.filesBox.insert(len(self.filenameList),base)
		self.filesBox.pack(fill=tk.X)
		self.filesBox.select_set(len(self.filenameList) - 1)
	'''

	'''
	clear the canvas
	
	@return None
	'''
	def clearCanvas(self, event=None):
		if self.createdTurtle:
			self.turt.reset()

	'''
	main program
	'''	
	def main(self):
		print ('Entering main loop')
		self.root.mainloop()

if __name__ == "__main__":
	dapp = DisplayApp(1200, 675)
	dapp.main()

