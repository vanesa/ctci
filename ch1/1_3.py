""" 
Cracking the Coding Interview

URLify: Write a mathod to replace all spaces in a string with with '%20'. 
You may assume that the string has sufficient space at the end to hold the additional characters, and that
you are given the 'true' length of the string.

>>> urlify('Mr John Smith     ', 13)
'Mr%20John%20Smith'

"""

import unittest

def urlify(phrase, num):

	urlified = ''
	phrase = phrase.strip()

	for character in phrase:
		if character == ' ':
			urlified += '%20'
		else:
			urlified += character

	return urlified


class Test(unittest.TestCase):
	""" Test Cases """

	data = [
		('Hey how is everything going      ', 27, 'Hey%20how%20is%20everything%20going'),
		('Mr John Smith    ', 13, 'Mr%20John%20Smith')

	]

	def test_urlify(self):
		for [test_string, length, expected] in self.data:
			actual = urlify(test_string, length)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()

# if __name__ == '__main__':
# 	from doctest import testmod
# 	if testmod.failed() == 0:
# 		# Great!
# 		app.run(debug=True)