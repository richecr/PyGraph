from graph.nodes.SimpleNode import SimpleNode
from graph.edges.SimpleEdge import SimpleEdge

class SimpleGraph():
    """implementation of a simple graph."""
    nodes = []
    edges = []

    def __init__(self):
        pass

    def add_node(self, value):
        self.nodes.append(SimpleNode(value))

    def add_edge(self, node_a, node_b):
        self.edges.append(SimpleEdge("teste", node_a, node_b))
    
    def __str__(self):
        graph_string = ""
        for edge in self.edges:
            graph_string += edge.__str__()
            graph_string += "\n"
        
        return graph_string