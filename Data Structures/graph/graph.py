class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjVertices = []
    
    def addAdjVertices(self, vertexArray):
        self.adjVertices += vertexArray

v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)

v1.addAdjVertices([v2, v3])
v2.addAdjVertices([v1])
v3.addAdjVertices([v1])

v3.addAdjVertices([v4])
v4.addAdjVertices([v3])

# print(v1)
# print(v3.adjVertices)