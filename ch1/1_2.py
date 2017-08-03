""" 
Cracking the Coding Interview

Given two strings, write a method to decide if one is premutation of the other.

>>> checkPremutation1('asdfghd', 'dsafdgh')
True
>>> checkPremutation1('asdfghd', 'adsswwwwfdgh')
False
>>> checkPremutation2('asdfghd', 'dsafdgh')
True
>>> checkPremutation2('asdfghd', 'adsswwwwfdgh')
False
>>> checkPremutation2('', '')
True

"""

def checkPremutation1(word1, word2):

	if len(word1) != len(word2):
		return False

	word1 = sorted(word1)
	word2 = sorted(word2)

	if word1 != word2:
		return False
	return True

def checkPremutation2(word1, word2):

	for letter in word1:
		if word2.count(letter) != word1.count(letter):
			return False
	return True


if __name__ == '__main__':
	from doctest import testmod
	if testmod.failed() == 0:
		# All good! Test passed!
		app.run(debug=True)