from graph.vertex.SimpleVertex import SimpleVertex
from graph.edges.SimpleEdge import SimpleEdge

class SimpleGraph():
    """implementation of a simple graph."""
    vertices = []
    edges = []

    def __init__(self):
        pass

    def add_vertex(self, value):
        self.vertices.append(SimpleVertex(value))

    def add_edge(self, vertex_a, vertex_b):
        self.edges.append(SimpleEdge("teste", vertex_a, vertex_b))

    def num_vertex(self):
        return len(self.vertices)

    def num_edges(self):
        return len(self.edges)

    def __str__(self):
        graph_string = ""
        for edge in self.edges:
            graph_string += edge.__str__()
            graph_string += "\n"
        
        return graph_string