class Node:
    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

class BinaryTree:
    def __init__(self, root):
        self.root = root