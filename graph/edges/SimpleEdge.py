class SimpleEdge():
    vertex_a = None
    vertex_b = None
    name = None

    def __init__(self, name, vertex_a, vertex_b):
        self.name = name
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b
    
    def __str__(self):
        return self.vertex_a + " - " + self.vertex_b