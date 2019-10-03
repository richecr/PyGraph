
class VertexNotExistsException(Exception):
    def __str__(self):
        return "Vértice não existe"


class VertexDuplicatedException(Exception):
    def __str__(self):
        return "Vértice Duplicado"
