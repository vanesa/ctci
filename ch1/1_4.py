""" 
Cracking the Coding Interview

Palindrome Premutation: Given a string, write a function to check if it is a premutation of a palindrome.
The palindrome does not need to be limited to just dictionary words.

input: Tact Coa
Output: True (premutation: "taco cat", "atco cta", etc.)
"""
import unittest

def isPalPerm(phrase):

	phrase = (''.join((phrase.split()))).lower()
	unique = []

	for letter in phrase:
		if phrase.count(letter) % 2 == 0:
			pass
		elif phrase.count(letter) == 1 and len(unique) == 0:
			unique.append(letter)
		else:
			return False
	return True


class Test(unittest.TestCase):
	""" Test Cases """

	data = [
	('Tact Coa', True), ('dfdfrgghh', True), 
	('A man a plan a Canal panama', True), 
	('dfd frg gihh', False)
	]

	def test_isPalPerm(self):
		for [test_string, expected] in self.data:
			actual = isPalPerm(test_string)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()