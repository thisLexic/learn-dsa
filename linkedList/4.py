class LinkedList:
    def __init__(self, head):
        self.head = head

    def __str__(self):
        array = []
        currentNode = self.head
        while True:
            nextNode = currentNode.nextNode
            if nextNode:
                array.append(currentNode.value)
                currentNode = nextNode
            else:
                array.append(currentNode.value)
                return str(array)

    def reverse(self):
        # Time complexity of O(n)
        currentNode = self.head
        prevNodes = []
        while True:
            nextNode = currentNode.nextNode
            if nextNode:
                prevNodes.append(currentNode)
                currentNode = nextNode
            else:
                break
        self.head = currentNode
        for _ in range(len(prevNodes)):
            n = prevNodes.pop()
            n.nextNode = None
            currentNode.nextNode = n
            currentNode = n

    def reverse2(self):
        # Time complexity of O(n)
        currentNode = self.head
        prevNode = None
        nextNode = currentNode.nextNode
        while nextNode:
            currentNode.nextNode = prevNode

            prevNode = currentNode
            currentNode = nextNode
            nextNode = currentNode.nextNode
        currentNode.nextNode = prevNode
        self.head = currentNode

class Node:
    def __init__(self, value, nextNode=None):
        self.nextNode = nextNode
        self.value = value

n1 = Node(1)
ll = LinkedList(n1)

n2 = Node(2)
n1.nextNode = n2

n3 = Node(3)
n2.nextNode = n3

print(ll)
ll.reverse()
print(ll)
ll.reverse2()
print(ll)