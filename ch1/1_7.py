""" 
Cracking the Coding Interview

Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. Can you do this in place?

>>> rotatematrix([[0,0,0,0],[1,1,1,1],[1,1,1,1],[0,0,0,0]])
[[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]

"""

import unittest

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

	return matrix90

class Test(unittest.TestCase):
	data = [
		([
			[0, 0, 0, 0],
			[1, 1, 1, 1],
			[1, 1, 1, 1],
			[0, 0, 0, 0]
		], [
			[0, 1, 1, 0],
			[0, 1, 1, 0], 
			[0, 1, 1, 0], 
			[0, 1, 1, 0]
		]), ([
			[1, 0, 0],
			[1, 1, 1],
			[1, 1, 1]
		], [
			[1, 1, 1],
			[1, 1, 0],
			[1, 1, 0]
		]), ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
	]

	def test_rotatematrix(self):
		for [test_matrix, expected] in self.data:
			actual = rotatematrix(test_matrix)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
