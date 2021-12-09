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

n1 = Node(1)
ll = LinkedList(n1)

n2 = Node(2)
n1.nextNode = n2

n3 = Node(3)
n2.nextNode = n3

n4 = Node(4)
n3.nextNode = n4

print(ll)
# delete n2
n2.value = n3.value
n2.nextNode = n4
print(ll)