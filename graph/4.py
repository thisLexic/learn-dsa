from collections import deque
from graph import Vertex

def bfs(vertex, value):
    hashTable = {vertex: True}
    queue = deque()
    queue.append(vertex)
    while queue:
        curVertex = queue.popleft()
        
        if curVertex.value == value:
            return curVertex

        for adjVertex in curVertex.adjVertices:
            if not hashTable.get(adjVertex):
                hashTable[adjVertex] = True
                queue.append(adjVertex)
    
    return None



v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)

v1.addAdjVertices([v2, v3])
v2.addAdjVertices([v1])
v3.addAdjVertices([v1])

v3.addAdjVertices([v4])
v4.addAdjVertices([v3])

print("find", v4)
print("using v1", bfs(v1, 4))
print("using v2", bfs(v2, 4))
print("using v3", bfs(v3, 4))

print("find 5", bfs(v1, 5))