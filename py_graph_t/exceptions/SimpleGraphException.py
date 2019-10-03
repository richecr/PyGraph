
class VertexNotExistsException(Exception):
    def __str__(self):
        return "Vértice não existe"


class EdgeDuplicatedException(Exception):
    def __str__(self):
        return "Aresta Duplicada"
