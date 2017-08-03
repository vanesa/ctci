""" 
Cracking the Coding Interview

Given two strings, write a method to decide if one is premutation of the other.

>>> checkPremutation1('asdfghd', 'adsfdgh')
True
>>> checkPremutation1('asdfghd', 'adsswwwwfdgh')
False

"""

def checkPremutation1(word1, word2):

	word1 = sorted(word1)
	word2 = sorted(word2)

	if word1 != word2:
		return False
	return True


if __name__ == '__main__':
	from doctest import testmod
	if testmod.failed() == 0:
		# All good! Test passed!
		app.run(debug=True)