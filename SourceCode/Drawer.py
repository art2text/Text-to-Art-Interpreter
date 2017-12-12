##
# Drawer class which handles creating the final drawing given a list of representative chars
#	from a text file
# 
# Adam Carlson
# 11/26/2017
#
##

# Dependencies
import random
import string
import turtle

""" CONSTANTS """

# tested colors which fit well together
ACCEPTABLE_COLORS = ['#6465A5', '#6975A6' , '#F3E96B', '#F28A30', '#F05837']

class Drawer:
	""" Drawer class for Text-to-Art Interpreter. """
		
	"""
	Attributes:
		lettersList: list of file's representative letters
		turt: the turtle instance, which draws the picture
		windowHeight: canvas window height
		windowWidth: canvas window width
		letters2action: mapping between chars and the function the turtle should do on the canvas
		closenessFactor: a factor of how close to the canvas edges the turtle should travel
		allowedLetters: letters which the turtle will respond to (all other chars ignored)
	"""
	
	''' 
	Initializes the Drawer object. 
	'''
	def __init__(self, lettersList, turt, windowWidth, windowHeight, closenessFactor = 0.1, testClass = False):
		self.lettersList = lettersList
		# for testing purposes, just use regular non-canvas turtle
		if testClass:
			self.turt = turtle
		else:
			self.turt = turt
		self.windowHeight = windowHeight
		self.windowWidth = windowWidth
		self.letters2action = self.buildMapping()
		self.closenessFactor = closenessFactor
		self.allowedLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		
		self.setupGraphics()
	
	'''
	setup the basic turtle graphics

	@return None
	'''
	def setupGraphics(self):
		# hide turtle icon
		self.turt.hideturtle()
		# set to max speed
		self.turt.speed(0)
		# set starting color
		self.turt.color(ACCEPTABLE_COLORS[0])
	
	'''
	build the mapping between chars and the turtle's actions
	
	@param turnAngle (int), angle turtle will turnt
	@param forwardDistance (int), pixel distance turtle can travel
	@param turtleGoToPadding (int), padding from edges when goto turtle method called
	@return finalMapping (dict), mapping between chars and turtle commands
	'''
	def buildMapping(self, turnAngle = 20, forwardDistance = 20, turtleGoToPadding = 50):
		finalMapping = {}
		
		# mappings for vowels
		finalMapping['a'] = (self.turt.right, turnAngle)
		finalMapping['e'] = (self.turt.right, turnAngle)
		finalMapping['i'] = (self.turt.right, turnAngle)
		finalMapping['o'] = (self.turt.right, turnAngle)
		finalMapping['u'] = (self.turt.right, turnAngle)
		
		''' @OldVersion
		# mappings for vowels
		finalMapping['a'] = (self.turt.left, turnAngle - 5)
		finalMapping['e'] = (self.turt.right, turnAngle + 5)
		finalMapping['i'] = (self.turt.left, turnAngle)
		finalMapping['o'] = (self.turt.right, turnAngle - 5)
		finalMapping['u'] = (self.turt.left, turnAngle + 5)
		'''
		
		# mappings for consonants
		finalMapping['b'] = (self.turt.color, ACCEPTABLE_COLORS[0])
		finalMapping['c'] = (self.turt.forward, forwardDistance)
		finalMapping['d'] = (self.turt.forward, forwardDistance)
		finalMapping['f'] = (self.turt.color, ACCEPTABLE_COLORS[1])
		finalMapping['g'] = (self.turt.forward, forwardDistance)
		finalMapping['h'] = (self.turt.forward, forwardDistance)
		finalMapping['j'] = (self.turt.forward, forwardDistance)
		finalMapping['k'] = (self.turt.color, ACCEPTABLE_COLORS[2])
		finalMapping['l'] = (self.turt.forward, forwardDistance)
		finalMapping['m'] = (self.turt.forward, forwardDistance)
		finalMapping['n'] = (self.turt.forward, forwardDistance)
		finalMapping['p'] = (self.turt.color, ACCEPTABLE_COLORS[3])
		finalMapping['q'] = (self.goto, (-1 * self.windowWidth * 0.5 + turtleGoToPadding, self.windowHeight * 0.5))
		finalMapping['r'] = (self.turt.forward, forwardDistance)
		finalMapping['s'] = (self.turt.color, ACCEPTABLE_COLORS[4])
		finalMapping['t'] = (self.turt.forward, forwardDistance)
		finalMapping['v'] = (self.turt.forward, forwardDistance)
		finalMapping['w'] = (self.goto, (self.windowWidth * 0.5 - turtleGoToPadding, -1 * self.windowHeight * 0.5))
		finalMapping['x'] = (self.goto, (-1 * self.windowWidth * 0.5 + turtleGoToPadding, -1 * self.windowHeight * 0.5))
		finalMapping['y'] = (self.turt.forward, forwardDistance)
		finalMapping['z'] = (self.goto, (self.windowWidth * 0.5 - turtleGoToPadding, self.windowHeight * 0.5))
		
		''' @OldVersion
		# mappings for consonants
		finalMapping['b'] = (self.turt.color, '#6465A5')
		finalMapping['c'] = (self.turt.forward, 15)
		finalMapping['d'] = (self.turt.forward, 10)
		finalMapping['f'] = (self.turt.color, '#6975A6')
		finalMapping['g'] = (self.turt.forward, 20)
		finalMapping['h'] = (self.turt.forward, 5)
		finalMapping['j'] = (self.turt.forward, 10)
		finalMapping['k'] = (self.turt.color, '#F3E96B')
		finalMapping['l'] = (self.turt.forward, 15)
		finalMapping['m'] = (self.turt.forward, 15)
		finalMapping['n'] = (self.turt.forward, 10)
		finalMapping['p'] = (self.turt.color, '#F28A30')
		finalMapping['q'] = (self.goto, (-1 * self.windowWidth * 0.5 + turtleGoToPadding, self.windowHeight * 0.5))
		finalMapping['r'] = (self.turt.forward, 25)
		finalMapping['s'] = (self.turt.color, '#F05837')
		finalMapping['t'] = (self.turt.forward, 20)
		finalMapping['v'] = (self.turt.forward, 5)
		finalMapping['w'] = (self.goto, (self.windowWidth * 0.5 - turtleGoToPadding, -1 * self.windowHeight * 0.5))
		finalMapping['x'] = (self.goto, (-1 * self.windowWidth * 0.5 + turtleGoToPadding, -1 * self.windowHeight * 0.5))
		finalMapping['y'] = (self.turt.forward, 15)
		finalMapping['z'] = (self.goto, (self.windowWidth * 0.5 - turtleGoToPadding, self.windowHeight * 0.5))
		'''
		
		return finalMapping
	
	'''
	Takes turtle to a given position and draws a circle. Then returns to original position
	
	@param  pos (tuple), x and y corrdinates of turtle
	@param circRadius (int), pixel radius of circle
	@return None
	'''
	def goto(self, pos, circRadius = 50):
		# current turtle location
		currPos = self.turt.position()
		
		# go to new location
		self.turt.up()
		self.turt.goto(pos[0], pos[1])
		self.turt.down()
		
		# create the circle
		self.turt.circle(circRadius)
		
		# return to original location
		self.turt.up()
		self.turt.goto(currPos)
		self.turt.down()
	
	'''
	Adjusts turtle's orientation if too close to the edges of the canvas
	
	@return None
	'''
	def adjustOrientation(self):
		# gets turtle's current position
		x = self.turt.pos()[0]
		y = self.turt.pos()[1]
		
		# determines how close to edges we will allow
		closenessFactor = self.closenessFactor
		
		# numbering of edge regions
		'''
		1	2	3
		4		5
		6	7	8
		'''
		
		# region 3 correction
		if x > self.windowWidth * (0.5 - closenessFactor) and y > self.windowWidth * (0.5 - closenessFactor):
			self.turt.setheading(225)
		# region 1 correction
		elif x < -1 * self.windowWidth * (0.5 - closenessFactor) and y > self.windowWidth * (0.5 - closenessFactor):
			self.turt.setheading(315)
		# region 2 correction
		elif y > self.windowWidth * (0.5 - closenessFactor):
			self.turt.setheading(270)
		# region 6 correction	
		elif x < -1 * self.windowWidth * (0.5 - closenessFactor) and y < -1 * self.windowWidth * (0.5 - closenessFactor):
			self.turt.setheading(45)
		# region 4 correction
		elif x < -1 * self.windowWidth * (0.5 - closenessFactor):
			self.turt.setheading(0)
		# region 8 correction	
		elif x > self.windowWidth * (0.5 - closenessFactor) and y < -1 * self.windowWidth * (0.5 - closenessFactor):
			self.turt.setheading(135)
		# region 7 correction
		elif y < -1 * self.windowWidth * (0.5 - closenessFactor):
			self.turt.setheading(90)
		# region 5 correction	
		elif x > self.windowWidth * (0.5 - closenessFactor):
			self.turt.setheading(180)
	
	'''
	draws the final image on the canvas
	
	@return None
	'''			
	def draw(self):
		
		# lettersList was not a list!	
		if not isinstance(self.lettersList, list):
			print ("Letters list was not a list!")
			return
			
		# do not render drawing if list was too big, to prevent crashing
		if len(self.lettersList) > 10000:
			print (len(self.lettersList))
			print ("Letters list was too large")
			return
		
		counter = 0
		
		# loop through list of file's representative chars
		for letter in self.lettersList:
			# reorient turtle if near edge
			self.adjustOrientation()
			
			# skip all non-lowercase letters
			if letter not in self.allowedLetters:
				continue
				
			# get the method and parameters for the turtle call
			storedAction = self.letters2action[letter]
			method = storedAction[0]
			parameter = storedAction[1]

			# call turtle method	
			method(parameter)
			
			# gradually increase closenessFactor as image is created 
			if counter % len(self.lettersList) // 2 == 0 and counter != 0:
				self.closenessFactor = max(0.01, self.closenessFactor - 0.01)
			counter += 1


'''
Test Drawer functionality
'''
def main():
	
	#TC12 empty letters array input
	print ("Empty character list input")
	d = Drawer(lettersList = [], turt = None, windowWidth = 100, windowHeight = 100, closenessFactor = 0.1, testClass = True)
	d.draw()
	input('Wait for keyboard response to move on:\n')
	turtle.clear()
	
	#TC13 array of non-alphabetic chars < 10,000
	print ("array of non-alphabetic chars < 10,000:")
	lettersList = [2] * 8000
	d = Drawer(lettersList = lettersList, turt = None, windowWidth = 100, windowHeight = 100, closenessFactor = 0.1, testClass = True)
	d.draw()
	input('Wait for keyboard response to move on:\n')
	turtle.clear()
	
	#TC14 array of non-alphabetic chars > 10,000
	print ("array of non-alphabetic chars > 10,000:")
	lettersList = [2] * 13000
	d = Drawer(lettersList = lettersList, turt = None, windowWidth = 100, windowHeight = 100, closenessFactor = 0.1, testClass = True)
	d.draw()
	input('Wait for keyboard response to move on:\n')
	turtle.clear()
	
	#TC15 array of alphabetic chars < 10,000
	print ("array of alphabetic chars < 10,000:")
	lettersList = ['t', 'a', 'p', 'e'] * 50
	d = Drawer(lettersList = lettersList, turt = None, windowWidth = 100, windowHeight = 100, closenessFactor = 0.1, testClass = True)
	d.draw()
	input('Wait for keyboard response to move on:\n')
	turtle.clear()
	
	#TC16 array of alphabetic chars > 10,000
	print ("array of alphabetic chars > 10,000:")
	lettersList = ['t', 'a', 'p', 'e'] * 6000
	d = Drawer(lettersList = lettersList, turt = None, windowWidth = 100, windowHeight = 100, closenessFactor = 0.1, testClass = True)
	d.draw()
	input('Wait for keyboard response to move on:\n')
	turtle.clear()
	
	#TC17 accidentally receives boolean instead of lettersList
	print ("boolean input:")
	lettersList = True
	d = Drawer(lettersList = lettersList, turt = None, windowWidth = 100, windowHeight = 100, closenessFactor = 0.1, testClass = True)
	d.draw()
	input('Wait for keyboard response to move on:\n')
	turtle.clear()
	
	#TC18 accidentally receives integer instead of lettersList
	print ("integer input:")
	lettersList = 50
	d = Drawer(lettersList = lettersList, turt = None, windowWidth = 100, windowHeight = 100, closenessFactor = 0.1, testClass = True)
	d.draw()
	input('Wait for keyboard response to move on:\n')
	turtle.clear()
	
	#TC19 accidentally receives String instead of lettersList
	print ("string input:")
	lettersList = 'test'
	d = Drawer(lettersList = lettersList, turt = None, windowWidth = 100, windowHeight = 100, closenessFactor = 0.1, testClass = True)
	d.draw()
	input('Wait for keyboard response to move on:\n')
	turtle.clear()
	
	#TC20 accidentally receives object instead of lettersList
	print ("object input:")
	lettersList = Drawer(lettersList = [], turt = None, windowWidth = 100, windowHeight = 100, closenessFactor = 0.1, testClass = True)
	d = Drawer(lettersList = lettersList, turt = None, windowWidth = 100, windowHeight = 100, closenessFactor = 0.1, testClass = True)
	d.draw()
	input('Wait for keyboard response to move on:\n')
	turtle.clear()
	
	#TC21 accidentally receives Float instead of lettersList
	print ("float input:")
	lettersList = 3.14159
	d = Drawer(lettersList = lettersList, turt = None, windowWidth = 100, windowHeight = 100, closenessFactor = 0.1, testClass = True)
	d.draw()
	input('Wait for keyboard response to move on:\n')  
	turtle.clear()         

if __name__ == '__main__':
	main()


