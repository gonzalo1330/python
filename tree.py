from collections import deque

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	
	def insert(self, value):
		if value < self.value:
			if self.left is None:
				self.left = Node(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = Node(value)
			else:
				self.right.insert(value)

class BinaryTreeIterator:
	def __init__(self, root):
		self.treeTraversed = deque()
		self.inOrderTraversal(root)
		print(self.treeTraversed)

	def hasNext(self):
		return len(self.treeTraversed) != 0
	
	def next(self):
		# TODO: change the pop(0) to be a deque to be more efficient
		print(self.treeTraversed.popleft())
	
	def inOrderTraversal(self, root):
		if root.left:
			self.inOrderTraversal(root.left)
		self.treeTraversed.append(root.value)
		if root.right:
			self.inOrderTraversal(root.right)