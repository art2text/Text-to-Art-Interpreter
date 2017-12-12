##
# DataStorage class to handle storing the application's past drawings for future use.
# All drawings are stored as a list of representative characters of the original text file used.
# 
# Adam Carlson
# 11/24/2017
#
##

# library dependency
import os

class DataStorage:
	""" DataStorage class for Text-to-Art Interpreter. """
	
	"""
	Attributes:
		fileStorageName: filename where we store past drawings
	"""
	
	'''
	initializes the DataStorage object.
	'''
	def __init__(self):
		self.fileStorageName = 'drawings.txt'
	
	
	'''
	Retrieves all past drawings.
	
	@returns an array of tuples, each with the form (filename, ['a', 'e', 'q', ...]) where
		the second item in the tuple is a list of representative chars for the given file.
		Each of these tuples gives us enough information to recreate past drawings.
	'''	
	def getData(self):
		
		# list of tuples, each with the form (filename, ['a', 'e', 'q', ...])
		drawings = []
		
		# read in the content from our storage file
		with open(self.fileStorageName) as file:
			content = file.read().splitlines()
		
		# populate our drawings list
		for i in range(0, len(content), 2):
			filename = content[i]
			drawing = content[i + 1].split(' ')
			drawings.append((filename, drawing))
		
		'''@OldVersion	
		# populate our drawings list
		for i in range(len(content)):
			drawing = content[i].split(' ')
			drawings.append((filename, drawing))
		'''
			
		file.close()
		
		return drawings
	
	
	'''
	Saves a drawing to our storage file.
	
	@param drawingData (list), list of representative characters for the text we are drawing
	@param filename (string), name of the text file we were drawing
	@returns None
	'''		
	def saveData(self, drawingData, filename):
		# final string we will write to our storage file
		stringRepresentationOfData = ''
		
		# start a new line if not first entry in storage
		if not os.stat(self.fileStorageName).st_size == 0:
			stringRepresentationOfData += '\n'
		
		# first add the filename	
		stringRepresentationOfData += filename
		stringRepresentationOfData += '\n'
		
		# loop through drawingData and append the chars to our string
		counter = 0
		for letter in drawingData:
			if counter is 0:
				stringRepresentationOfData += letter
			else:
				stringRepresentationOfData += (' ' + letter)
			counter += 1
			
		# write our string representation of the drawing to our storage file
		file = open(self.fileStorageName, "a")
		file.write(stringRepresentationOfData)
		file.close()
		
	''' @OldVersion
	def saveData(self, drawingData):
		# final string we will write to our storage file
		stringRepresentationOfData = ''
		
		# loop through drawingData and append the chars to our string
		counter = 0
		for letter in drawingData:
			if counter is 0:
				stringRepresentationOfData += letter
			else:
				stringRepresentationOfData += (' ' + letter)
			counter += 1
			
		# write our string representation of the drawing to our storage file
		file = open(self.fileStorageName, "a")
		file.write(stringRepresentationOfData)
		file.close()
	'''
	