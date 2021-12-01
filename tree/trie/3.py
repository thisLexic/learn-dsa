class Node:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        curNode = self.root
        for c in string:
            if not curNode.children.get(c):
                curNode.children[c] = Node()
            curNode = curNode.children[c]
        curNode.children["*"] = None
    
    def printKeys(self, curNode=None):
        curNode = curNode or self.root
        for key, childNode in curNode.children.items():
            print(key)
            if childNode:
                self.printKeys(childNode)

t = Trie()
t.insert("bake")
t.insert("bat")
t.insert("bats")
t.insert("battery")

t.printKeys()