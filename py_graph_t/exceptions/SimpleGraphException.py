
class VertexNotExistsException(Exception):
    def __str__(self):
        return "Vértice não existe"


class EdgeDuplicatedException(Exception):
    def __str__(self):
        return "Aresta duplicada"

class EdgeNotFoundException(Exception):
    def __str__(self):
        return "Aresta não existe"

class VertexDuplicatedException(Exception):
    def __str__(self):
        return "Vértice duplicado"