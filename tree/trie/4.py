class Node:
    def __init__(self):
        self.children = {}

    def getAnySection(self):
        keys = self.children.keys()
        if keys:
            key = list(keys)[0]
            if self.children[key]:
                return key + self.children[key].getAnySection()
        return ""

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

    def autocorrect(self, string):
        curNode = self.root
        for i in range(len(string)):
            c = string[i]
            if curNode.children.get(c):
                curNode = curNode.children[c]
            else:
                return string[:i] + curNode.getAnySection()
        return string

t = Trie()
t.insert("bake")
t.insert("bat")
t.insert("bats")
t.insert("battery")
t.insert("battles")

l = "b"
print(l,":",t.autocorrect(l))
l = "ba"
print(l,":",t.autocorrect(l))
l = "bat"
print(l,":",t.autocorrect(l))
l = "batt"
print(l,":",t.autocorrect(l))
l = "battz"
print(l,":",t.autocorrect(l))
l = "battzzzzz"
print(l,":",t.autocorrect(l))
l = "battlej"
print(l,":",t.autocorrect(l))