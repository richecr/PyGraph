from graph.vertex.SimpleVertex import SimpleVertex
from graph.edges.SimpleEdge import SimpleEdge

class SimpleGraph():
    """implementation of a simple graph."""
    vertices = []
    edges = []

    def __init__(self):
        pass

    def add_vertex(self, value):
        """
        Método que adiciona um vértice ao grafo.

        Parâmetros:
        ----------
        value: Um tipo existente ou criado por você
            - Valor a ser colocado no vértice.
        """
        self.vertices.append(SimpleVertex(value))

    def add_edge(self, name=None, vertex_a=None, vertex_b=None):
        """
        Método que adiciona uma aresta ao grafo.

        Parâmetros:
        ----------
        name: String
            - Nome da aresta do grafo.
        vertex_a: Tipo dos vértices.
            - Vértice cabeça da aresta.
        vertex_b: Tipo dos vértices.
            - Vértice cauda da aresta.
        """
        self.edges.append(SimpleEdge( name=name, vertex_a=vertex_a, vertex_b=vertex_b))

    def num_vertex(self):
        """
        Método que retorna o número de vértices no grafo.

        Retorno:
        ----------
        Quantidade: Int
            - Quantidade de número de vértices.
        """
        return len(self.vertices)

    def num_edges(self):
        """
        Método que retorna o número de arestas no grafo.

        Retorno:
        ----------
        Quantidade: Int
            - Quantidade de número de arestas.
        """
        return len(self.edges)

    def __str__(self):
        """
        Método que retorna a representação textual do grafo.

        Retorno:
        ----------
        graph_string: String
            - Representação textual do grafo.
        """
        graph_string = ""
        for edge in self.edges:
            graph_string += edge.__str__()
            graph_string += "\n"
        
        return graph_string