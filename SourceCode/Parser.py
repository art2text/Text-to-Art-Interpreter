##
# Parser class to interpret the contents of a text file
# 
# Lawrence Dickey
# 11/27/2017
#
##

class Parser:
	""" Parser class for Text-to-Art Interpreter. 

	Attributes:
		filename: name of the file to be parsed. 
		characters: list of characters
		file_length: the length of the file. 
	"""

	''' 
	Initializes the parser object for a file. Asks user for the name of a file. 
	'''
	def __init__(self, fn):
		# Store filename in class variable. 
		self.filename = fn
			

		# Initialize empty list for characters.
		self.characters = []
		
		# ignore non-text files
		if not fn.endswith('.txt'):
			print ("Please use a text file.")
			self.file_length = 0
			return

		# Store length of file.
		with open(self.filename, 'r') as file:
			text = file.read().strip().split()
			# Populate characters list with all characters within file. 
			for word in text:
				for character in word:
					self.characters.append(character)
			len_chars = sum(len(word) for word in text)

		# Store length of file as global variable. 
		self.file_length = len_chars


	'''  
	The method tests to see if there are more than 10,000 characters in the file parsed 
		in the init method. If there are > 10,000, it divides the number of characters 
		by 10,000, rounding down to the nearest integer. It then creates a new list, chars,
		to which it adds every n'th character where n * 10,000 ~= the number of characters in the file.
		
	@return chars (list), a list with up to 10,000 characters in it that are representative of the file. 
	'''
	def get_characters_list(self):
		chars = []
		# File has > 10,000 characters:
		if (self.file_length > 10000):
			iterator_range = float(self.file_length) / 10000.0 # Computer distance between characters to analize within the self.characters list. 
			iterator_range = int(iterator_range) # Round down to nearest integer. 
			chars = [] # List to return
			i = 0
			for char in range(int(self.file_length / iterator_range)):
				chars.append(self.characters[iterator_range * i]) 
				i += 1 # Increment iteration variable.
			chars = chars[:9999]
			return chars
		# File has < 10,000 characters
		else:
			chars = [] # List to return
			i = 0
			for char in range(self.file_length):
				chars.append(self.characters[i])
				i += 1 # Increment iteration variable. 
		return chars
		
	''' @OldVersion
	def get_characters_list(self):
		chars = [] # List to return
		i = 0
		for char in range(self.file_length):
			chars.append(self.characters[i])
			i += 1 # Increment iteration variable. 
		return chars
	'''
		

''' 
Test Parser functionality
'''
def main():
	
	# TC01: non-text file input
	print ("Test non-text file:")
	parser = Parser('../TestFiles/ExampleFile.csv')
	print (parser.get_characters_list())
	print ('\n')
	
	# TC02: empty file input
	print ("Test empty input:")
	parser = Parser('')
	print (parser.get_characters_list())
	print ('\n')
	
	# TC03: short non-alphabetic input (< 100 chars)
	print ("Test short non-alphabetic input (< 100 chars):")
	parser = Parser('../TestFiles/ShortNonAlphabetic.txt')
	print (parser.get_characters_list())
	print ('\n')
	
	# TC04: medium non-alphabetic input (< 10,000 chars)
	print ("Test medium non-alphabetic input (< 10,000 chars):")
	parser = Parser('../TestFiles/MediumNonAlphabetic.txt')
	print (parser.get_characters_list())
	print ('\n')
	
	# TC05: large non-alphabetic input (< 100,000 chars)
	print ("Test large non-alphabetic input (< 100,000 chars):")
	parser = Parser('../TestFiles/LargeNonAlphabetic.txt')
	print (parser.get_characters_list())
	print ('\n')
	
	# TC06: short alphabetic input (< 100 chars)
	print ("Test short alphabetic input (< 100 chars):")
	parser = Parser('../TestFiles/ShortAlphabetic.txt')
	print (parser.get_characters_list())
	print ('\n')
	
	# TC07: medium alphabetic input (< 10,000 chars)
	print ("Test medium alphabetic input (< 10,000 chars):")
	parser = Parser('../TestFiles/MediumAlphabetic.txt')
	print (parser.get_characters_list())
	print ('\n')
	
	# TC08: large alphabetic input (< 100,000 chars)
	print ("Test large alphabetic input (< 100,000 chars):")
	parser = Parser('../TestFiles/LargeAlphabetic.txt')
	print (parser.get_characters_list())
	print ('\n')
	
	# TC09: short alphabetic/non-alphabetic mix input (< 100 chars)
	print ("Test short alphabetic/non-alphabetic mix input (< 100 chars):")
	parser = Parser('../TestFiles/ShortMixed.txt')
	print (parser.get_characters_list())
	print ('\n')
	
	# TC10: medium alphabetic/non-alphabetic mix input (< 10,000 chars)
	print ("Test medium alphabetic/non-alphabetic mix input (< 10,000 chars):")
	parser = Parser('../TestFiles/MediumMixed.txt')
	print (parser.get_characters_list())
	print ('\n')
	
	# TC11: large alphabetic/non-alphabetic mixed input (< 100,000 chars)
	print ("Test large alphabetic/non-alphabetic mixed input (< 100,000 chars):")
	parser = Parser('../TestFiles/LargeMixed.txt')
	print (parser.get_characters_list())
	print ('\n')
	

if __name__ == '__main__':
	main()



