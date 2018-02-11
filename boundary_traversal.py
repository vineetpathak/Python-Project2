# -*- coding: UTF-8 -*-

# Boundary Traversal

'''
	Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root.
'''
import binary_tree

def printBoundaryLeft(root):
	'''Print left boundary of the tree'''
	if not root:
		return

	if root.left:
		print root.data
		printBoundaryLeft(root.left)
	elif root.right:
		print root.right
		printBoundaryLeft(root.right)

def printLeaves(root):
	'''Print leaf nodes of a binary tree'''
	if not root:
		return

	printLeaves(root.left)

	if not root.left and not root.right:
		print root.data

	printLeaves(root.right)

def printBoundaryRight(root):
	'''Print right boundary of the binary tree'''
	if not root:
		return

	if root.right:
		print root.data
		printBoundaryRight(root.right)
	elif root.left:
		print root.data
		printBoundaryRight(root.left)

def printBoundary(root):
	'''Print the boundary traversal of a tree'''
	if not root:
		return

	print root.data
	printBoundaryLeft(root.left)

	printLeaves(root.left)
	printLeaves(root.right)

	printBoundaryRight(root.right)

if __name__ == "__main__":
	tree = binary_tree.construct_binary_tree()
	printBoundary(tree.root)
