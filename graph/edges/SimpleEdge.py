class SimpleEdge():
    node_a = None
    node_b = None
    name = None

    def __init__(self, name, node_a, node_b):
        self.name = name
        self.node_a = node_a
        self.node_b = node_b
    
    def __str__(self):
        return self.node_a + " - " + self.node_b