""" 
Cracking the Code Interview Excercises 

Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

>>> isUnique('asdfghjkl')
True

>>> isUnique('asdfghajks')
False

>>> isUnique2('asdfghjkl')
True

>>> isUnique2('asdfghjkss')
False

"""

""" With datastructure Dictionary """
def isUnique(word):
	word_dict = {}
	for letter in word:
		if letter in word_dict:
			return False
		word_dict[letter] = True
	return True

""" Without datastructures """

def isUnique2(word):
	for letter1 in range(len(word)):
		for letter2 in word[letter1+1:]:
			if word[letter1] == letter2:
				return False
	return True


if __name__ == "__main__":
	from doctest import testmod
	if testmod().failed == 0:
		app.run(debug==True)
		print 'All the tests passed. Awesome!'