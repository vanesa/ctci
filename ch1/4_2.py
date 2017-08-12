"""
Cracking the code Interview

Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

Input: [1,2,3,6,8,9,11,14,17,20]
Output: 

"""

class Node(object):

	def __init__(self, root, left = None, right = None):
		self.root = root
		self.left = left
		self.right = right


def initialize_bst(array):
	return (array, 0, len(array)-1)

def build_bst(array, start, end):
    
    if start > end:
        return None
        
    mid = int((start+end)/2)
    root = Node(array[mid])
    root.left = build_bst(array, start, mid-1)
    root.right = build_bst(array, mid+1, end)

    return root


array, start, end = initialize_bst([1,2,3,6,8,9,11,14,17,20])
build_bst(array, start, end)