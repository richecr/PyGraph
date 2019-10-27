class ValueBinding:
    """
    Classe que representa uma ligação de incidência de um
    vértice e a aresta de um grafo.
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

    def __eq__(self, other):
        """
        Método para comparação de duas arestas

        Parâmetros:
        ---------
        other: ValueBinding
            - aresta a ser comparada
        """
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __repr__(self):
        result = str(self.vertex_name) + " - "
        result += str(self.edge_name) + " => "
        result += str(self.value)
        return result
