""" 
Cracking the Coding Interview

Palindrome Premutation: Given a string, write a function to check if it is a premutation of a palindrome.
The palindrome does not need to be limited to just dictionary words.

input: Tact Coa
Output: True (premutation: "taco cat", "atco cta", etc.)
"""

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
