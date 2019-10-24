class ValueBinding:
    """
    Classe que representa uma ligação de incidência de um vértice e a aresta de um grafo.
    """

    def __init__(self, vertex_name, edge_name, value):
        """
        Inicialização dos atributos da classe ValueBinding.
        """
        self.vertex_name = vertex_name
        self.edge_name = edge_name
        self.value = value
    
    def get_vertex_name(self):
        return self.vertex_name

    def get_edge_name(self):
        return self.edge_name

    def get_value(self):
        return self.value
    
    def __repr__(self):
        return str(self.vertex_name) + " - " + str(self.edge_name) + " => " + str(self.value)