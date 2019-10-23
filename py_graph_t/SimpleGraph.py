from .vertex.SimpleVertex import SimpleVertex
from .edges.SimpleEdge import SimpleEdge
from .Graph import Graph

from .exceptions.SimpleGraphException import VertexNotExistsException, EdgeDuplicatedException, EdgeNotFoundException, VertexDuplicatedException, CycleDetectedException

class SimpleGraph(Graph):
    """
    Implementação de um Grafo Simples. 
    
    Um grafo simples ``não contém``:
        - Loops
        - Arestas paralelas

    Nessa implementação as ``arestas não tem pesos``.
    """

    def __init__(self):
        super().__init__()
        pass

    def add_edge(self, value_a, value_b, name=None):
        """
        Método que adiciona uma aresta ao grafo.

        Parâmetros:
        ----------
        value_a:
            - Identificador do vértice cabeça da aresta.
        value_b:
            - Identificador do vértice cauda da aresta.
        name: String
            - Nome da aresta do grafo.
        """
        vertex_a = self.vertices.get(value_a)
        vertex_b = self.vertices.get(value_b)
        new_edge = SimpleEdge(name=name, vertex_a=vertex_a, vertex_b=vertex_b)

        if vertex_a is None or vertex_b is None:
            raise VertexNotExistsException()
        if new_edge in self.edges:
            raise EdgeDuplicatedException()
        else:
            self.edges.append(new_edge)
            if self.has_loop():
                self.edges.remove(new_edge)
                raise CycleDetectedException()
            else:
                return self.show_edge(value_a, value_b)