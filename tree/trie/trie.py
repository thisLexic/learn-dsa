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

# Populate
t = Trie()
t.insert("bake")
t.insert("bat")
t.insert("bats")
t.insert("battery")

# Check
print(t.root.children["b"].children["a"].children)
print(t.root.children["b"].children["a"].children["t"].children)