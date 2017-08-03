""" 
Cracking the Coding Interview

Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. Can you do this in place?

>>> rotatematrix([[0,0,0,0],[1,1,1,1],[1,1,1,1],[0,0,0,0]])
[[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]

"""

def rotatematrix(matrix):

	matrix90 = []
	row90 = []

	num = 0
	while num < len(matrix):
		for i in range(len(matrix)-1, -1, -1):
			row90.append(matrix[i][num])
		matrix90.append(row90)
		row90 = []
		num += 1

	print matrix90


if __name__ == '__main__':
	from doctest import testmod
	if testmod.failed() == 0:
		# High five!
		app.run(debug=True)