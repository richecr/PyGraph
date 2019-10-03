from .vertex.SimpleVertex import SimpleVertex
from .edges.SimpleEdge import SimpleEdge

from .exceptions.SimpleGraphException import VertexNotExistsException

class SimpleGraph():
    """Implementação de um simples grafo."""
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

    def delete_vertex(self, vertex):
        """
        Método que remove um vertice do grafo e consequentemente todas as arestas
        conectadas ao vertice.

        Parâmetros:
        ----------
        vertex: SimpleVertex
            - vértice a ser removido
        """

        if (self.vertex_exists(vertex)):
            for i in range(len(self.edges)-1,-1,-1):

                edge = self.edges[i]
                if (self.is_terminal(edge, vertex)):
                    self.edges.pop(i)

            self.vertices.remove(vertex)

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

    def delete_edge(self, vertex_a, vertex_b):
        """
        Método que remove uma aresta do grafo.

        Parâmetros:
        ----------
        edge: SimpleEdge
            - Aresta a ser removida.
        """
        edge_aux = SimpleEdge(vertex_a=vertex_a, vertex_b=vertex_b)
        if (self.edges.__contains__(edge_aux)):
            self.edges.remove(edge_aux)
        else:
            return

    def is_terminal(self, edge, vertex):
        """
        Método que verifica se um dado vértice é terminal de uma dada aresta.
        
        Parâmetros:
        ----------
            edge: SimpleEdge
                - Aresta a ser verificada.
            vertex: SimpleVertex
                - vertice a ser verificado.
        
        Retorno:
        ----------
        Resultado: bool
            - Valor booleano indicando se o vértice é um dos terminais da aresta.
        """
        return edge.vertex_a == vertex.value or edge.vertex_b == vertex.value

    def num_vertex(self):
        """
        Método que retorna o número de vértices no grafo.

        Retorno:
        ----------
        Quantidade: Int
            - Quantidade de número de vértices.
        """
        return len(self.vertices)

    def vertex_exists(self,vertex):
        """
        Método booleano que indica se um determinado vértice pertence ao Grafo.

        Parâmetros:
        ----------
        vertex: SimpleVertex
            - vértice a ser verificado
           
        """
        return self.vertices.__contains__(vertex)

    def edge_exists(self,edge):
        """
        Método booleano que indica se um determinada aresta pertence ao Grafo.

        Parâmetros:
        ----------
        edge: SimpleEdge
            - aresta a ser verificada
           
        """
        return self.edges.__contains__(edge)

    def num_edges(self):
        """
        Método que retorna o número de arestas no grafo.

        Retorno:
        ----------
        Quantidade: Int
            - Quantidade de número de arestas.
        """
        return len(self.edges)

    def vertex_neighbors(self, value):
        """
        Método que retorna uma lista com os vértices vizinhos do vértice de entrada.

        Parâmetros:
        ----------
        value: *
            - Tipo do vértice de entrada.
        """
        neigh_vertices = []
        for edge in self.edges:
            if edge.vertex_a == value:
                neigh_vertices.append(edge.vertex_b)
            elif edge.vertex_b == value:
                neigh_vertices.append(edge.vertex_a)

        return neigh_vertices

    def vertex_degree(self, value):
        """
        Método que retorna o grau do vértice de entrada.

        Parâmetros:
        ----------
        value: *
            - Tipo do vértice de entrada.

        Retorno:
        ----------
        Quantidade: Int
            - Quantidade de vizinhos do vértice de entrada.
        """
        if(self.vertex_exists(value)):
            return len(self.vertex_neighbors(value))
        else:
            raise VertexNotExistsException()
    
    def vertices_adjacency(self, value_a, value_b):
        """
        Método booleano que indica se os vértices de entrada são adjacentes.

        Parâmetros:
        ----------
        vertex_a: *
            - Tipo dos vértices.
        vertex_b: *
            - Tipo dos vértices.
        """
        neigh_vertices = self.vertex_neighbors(value_a)
        if value_b in neigh_vertices:
            return True
        else:
            return False

    def get_all_vertex(self):
        """
        Método que retorna uma lista com os vértices do grafo.

        Retorno:
        ----------
        vertices: List
            - Lista com todos os vértices do grafo.
        """
        return self.vertices

    def list_graph_vertices(self):
        """
        Método que retorna lista com todos os valores dos vértices do grafo.
        """
        vertices = []
        for vertex in self.vertices:
            vertices.append(vertex.value)
        return vertices

    def list_graph_edges(self):
        """
        Método que retorna lista com todos os nomes as arestas do grafo.
        """
        edges = []
        for edge in self.edges:
            edges.append(edge.name)
        return edges
    
    def show_edge(self, vertex_a, vertex_b):
        """
        Método que retorna uma aresta entre dois vértices, se ela existe.
        """
        edge_a = SimpleEdge(vertex_a=vertex_a, vertex_b=vertex_b)      
        edge_b = SimpleEdge(vertex_a=vertex_b, vertex_b=vertex_a)

        for edge in self.edges:
            if edge == edge_a or edge == edge_b:
                return edge

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
