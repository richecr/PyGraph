from .vertex.SimpleVertex import SimpleVertex
from .edges.SimpleEdge import SimpleEdge
from .Graph import Graph

from .exceptions.SimpleGraphException import (
    VertexNotExistsException,
    EdgeDuplicatedException,
    EdgeNotFoundException,
    VertexDuplicatedException
)


class CompleteGraph(Graph):
    """
    Implementação de um Grafo Completo.

    Em um grafo completo ``todos os vértices`` são:
        - Adjacentes a todos os outros vértices

    Nessa implementação as ``arestas não tem pesos``.
    """
    def __init__(self):
        super().__init__()
        pass
