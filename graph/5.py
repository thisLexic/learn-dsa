from collections import deque
from graph import Vertex

def getShortestPath(startVertex, value):
    shortestPath = {startVertex: 0}
    shortestPrevVertexStopover = {startVertex: startVertex}
    queue = deque()
    queue.append(startVertex)

    while queue:
        curVertex = queue.popleft()
        
        if curVertex.value == value:
            path = [curVertex.value]
            # for k, v in shortestPrevVertexStopover.items():
            #     print(k.value, v.value)
            while True:
                if shortestPrevVertexStopover.get(curVertex) != startVertex:
                    curVertex = shortestPrevVertexStopover[curVertex]
                    path.append(curVertex.value)
                else:
                    path.append(startVertex.value)
                    path.reverse()
                    return path


        for adjVertex in curVertex.adjVertices:
            if shortestPath.get(adjVertex, -1) == -1:
                shortestPath[adjVertex] = 1 + shortestPath[curVertex]
                shortestPrevVertexStopover[adjVertex] = curVertex
                queue.append(adjVertex)
            else:
                if shortestPath[adjVertex] > 1 + shortestPath[curVertex]:
                    shortestPath[adjVertex] = 1 + shortestPath[curVertex]
                    shortestPrevVertexStopover[adjVertex] = curVertex
    
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

print(getShortestPath(v1, 4))