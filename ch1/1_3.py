""" 
Cracking the Coding Interview

URLify: Write a mathod to replace all spaces in a string with with '%20'. 
You may assume that the string has sufficient space at the end to hold the additional characters, and that
you are given the 'true' length of the string.

>>> urlify('Mr John Smith', 13)
'Mr%20John%20Smith'

"""

def urlify(phrase, num):

	urlified = ''
	for character in phrase:
		if character == ' ':
			urlified += '%20'
		else:
			urlified += character

	return urlified

if __name__ == '__main__':
	from doctest import testmod
	if testmod.failed() == 0:
		# Great!
		app.run(debug=True)