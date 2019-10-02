class SimpleEdge(object):
    vertex_a = None
    vertex_b = None
    name = None

    def __init__(self, name=None, vertex_a=None, vertex_b=None):
        if (name == None):
            name = vertex_a.__str__() + vertex_b.__str__()
        self.name = name
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.vertex_a == other.vertex_a and self.vertex_b == other.vertex_b
        else:
            return False

    def __str__(self):
        return self.name + ": " + self.vertex_a.__str__() + " -> " + self.vertex_b.__str__()
