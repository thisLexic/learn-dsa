class Node:
    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def max(self):
        curNode = self.root
        while True:
            if not curNode.rightNode:
                return curNode
            else:
                curNode = curNode.rightNode

n10 = Node(10)
bst = BinaryTree(n10)

n5 = Node(5)
n10.leftNode = n5

n3 = Node(3)
n5.leftNode = n3

n7 = Node(7)
n5.rightNode = n7

n20 = Node(20)
n10.rightNode = n20

n15 = Node(15)
n20.leftNode = n15

n25 = Node(25)
n20.rightNode = n25

print(bst.max().value)