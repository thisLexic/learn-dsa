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

class Node:
    def __init__(self, value, nextNode=None):
        self.nextNode = nextNode
        self.value = value

