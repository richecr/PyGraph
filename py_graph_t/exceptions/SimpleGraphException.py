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


class CycleDetectedException(Exception):
    def __str__(self):
        return "Esse tipo de grafo não pode conter ciclo"


class LoopDetectedException(Exception):
    def __str__(self):
        return "Esse tipo de grafo não pode conter loops"


class EdgeNameExistsException(Exception):
    def __str__(self):
        return "Aresta com esse nome já existe"
