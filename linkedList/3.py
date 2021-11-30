class LinkedList:
    def __init__(self, head):
        self.head = head

    def getTail(self):
        # Time complexity of O(n)
        currentHead = self.head
        while True:
            if currentHead.nextNode != None:
                currentHead = currentHead.nextNode
            else:
                return currentHead

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

print(ll.getTail().value)