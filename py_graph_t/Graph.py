from .vertex.SimpleVertex import SimpleVertex
from .edges.SimpleEdge import SimpleEdge
from .util.ValueBinding import ValueBinding

from .exceptions.SimpleGraphException import (
    VertexNotExistsException,
    EdgeNotFoundException,
    VertexDuplicatedException,
    EdgeNameExistsException
)


class Graph:
    """Implementação de um grafo base."""

    def __init__(self):
        self.vertices = dict()
        self.edges = []
        pass

    def add_vertex(self, value):
        """
        Método que adiciona um vértice ao grafo.

        Parâmetros:
        ----------
        value:
            - Valor a ser colocado no vértice.
            - Identificador do vértice.
        """
        if not self.vertices.__contains__(value):
            self.vertices[value] = SimpleVertex(value)
            return self.vertices[value]
        else:
            raise VertexDuplicatedException()

    def delete_vertex(self, value):
        """
        Método que remove um vertice do grafo e consequentemente todas
        as arestas
        conectadas ao vertice.

        Parâmetros:
        ----------
        value:
            - Identificador do vértice a ser removido
        """
        if self.vertex_exists(value):
            vertex_removed = self.vertices[value]
            for i in range(len(self.edges)-1, -1, -1):
                edge = self.edges[i]
                if self.is_terminal(edge, value):
                    self.edges.pop(i)

            self.vertices.__delitem__(value)
            return vertex_removed
        else:
            raise VertexNotExistsException()

    def show_edge(self, value_a, value_b):
        """
        Método que retorna uma aresta entre dois vértices, se ela
        existe.

        Parâmetros:
        ----------
        value_a:
            - Identificador do vértice.
        value_b:
            - Identificador do vértice.
        """
        vertex_a = self.vertices.get(value_a)
        vertex_b = self.vertices.get(value_b)

        if vertex_a is None or vertex_b is None:
            raise VertexNotExistsException

        edge_test = SimpleEdge(vertex_a=vertex_a, vertex_b=vertex_b)

        edge_out = None
        for edge in self.edges:
            if edge_test.__eq__(edge):
                edge_out = edge

        if edge_out is None:
            raise EdgeNotFoundException()

        return edge_out

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

        if vertex_a is None or vertex_b is None:
            raise VertexNotExistsException()

        if self.edge_name_exists(name):
            raise EdgeNameExistsException()

        new_edge = SimpleEdge(name=name, vertex_a=vertex_a, vertex_b=vertex_b)

        self.edges.append(new_edge)
        return self.show_edge(value_a, value_b)

    def edge_name_exists(self, name):
        for edge in self.edges:
            if edge.get_name() == name:
                return True
        return False

    def delete_edge(self, value_a, value_b):
        """
        Método que remove uma aresta do grafo.

        Parâmetros:
        ----------
        value_a:
            - Identificador do vértice cabeça da aresta.
        value_b:
            - Identificador do vértice cauda da aresta.
        """
        vertex_a = self.vertices.get(value_a)
        vertex_b = self.vertices.get(value_b)
        edge_aux = SimpleEdge(vertex_a=vertex_a, vertex_b=vertex_b)

        edge_out = None
        if self.edges.__contains__(edge_aux):
            index = self.edges.index(edge_aux)
            edge_out = self.edges[index]
            self.edges.remove(edge_aux)
        else:
            raise EdgeNotFoundException()

        return edge_out

    def is_terminal(self, edge, value):
        """
        Método que verifica se um dado vértice é terminal de uma
        dada aresta.

        Parâmetros:
        ----------
        edge: SimpleEdge
            - Aresta a ser verificada.
        value:
            - Identificador do vertice.

        Retorno:
        ----------
        resultado: bool
            - Valor booleano indicando se o vértice é um dos terminais
            da aresta.
        """
        return edge.vertex_a.value == value or edge.vertex_b.value == value

    def num_vertex(self):
        """
        Método que retorna o número de vértices no grafo.

        Retorno:
        ----------
        Quantidade: Int
            - Quantidade de número de vértices.
        """
        return len(self.vertices)

    def vertex_exists(self, value):
        """
        Método que indica se um determinado vértice pertence ao Grafo.

        Parâmetros:
        ----------
        value:
            - Identificador do vértice a ser verificado

        Retorno:
        ----------
        True: Caso o vertice pertença ao grafo.

        False: Caso não.
        """
        return self.vertices.__contains__(value)

    def edge_exists(self, value_a, value_b):
        """
        Método booleano que indica se um determinada aresta pertence
        ao Grafo.

        Parâmetros:
        ----------
        value_a:
            - Identificador do vértice cabeça da aresta.
        value_b:
            - Identificador do vértice cauda da aresta.

        Retorno:
        ----------
        True: caso a aresta exista.

        False: caso contrário.
        """
        vertex_a = self.vertices.get(value_a)
        vertex_b = self.vertices.get(value_b)
        edge_aux = SimpleEdge(vertex_a=vertex_a, vertex_b=vertex_b)

        if self.edges.__contains__(edge_aux):
            return True
        else:
            return False

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
        Método que encontra vertices vizinhos do vertice de entrada.

        Parâmetros:
        ----------
        value:
            - Identificador do vertice.

        Retorno:
        ----------
        neigh_vertices: List
            - Lista de vertices.
        """
        if self.vertex_exists(value):
            neigh_vertices = []
            for edge in self.edges:
                if edge.vertex_a.value == value:
                    neigh_vertices.append(edge.vertex_b)
                elif edge.vertex_b.value == value:
                    neigh_vertices.append(edge.vertex_a)
            return neigh_vertices
        else:
            raise VertexNotExistsException()

    def vertex_degree(self, value):
        """
        Método que retorna o grau do vértice de entrada.

        Parâmetros:
        ----------
        value:
            - Identificador do vertice.

        Retorno:
        ----------
        Grau: Int
            - Grau do vértice de entrada.
        """
        if self.vertex_exists(value):
            return len(self.vertex_neighbors(value))
        else:
            raise VertexNotExistsException()

    def is_vertices_adjacents(self, value_a, value_b):
        """
        Método que indica se os vértices de entrada são adjacentes.

        Parâmetros:
        ----------
        value_a:
            - Identificador do vértice.
        value_b:
            - Identificador do vértice.

        Retorno:
        ----------
        True: Caso os vertices sejam adjacentes.

        False: Caso contrario.
        """
        neigh_vertices = self.vertex_neighbors(value_a)
        vertex_b = self.vertices.get(value_b)
        if vertex_b in neigh_vertices:
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
        Método que retorna lista com todos os identificadores dos
        vértices do grafo.

        Retorno:
        ----------
        vertices: List
            - Lista com o nome de todas os vértices do grafo.
        """
        vertices = []
        for vertex in self.vertices:
            vertices.append(vertex)
        return vertices

    def list_graph_edges(self):
        """
        Método que retorna lista com todos os nomes as arestas
        do grafo.

        Retorno:
        ----------
        edges: List
            - Lista com o nome de todas as arestas do grafo.
        """
        edges = []
        for edge in self.edges:
            edges.append(edge.name)
        return edges

    def cycle(self, v, visited, parent):
        """
        Método que verifica se tem ciclo no subgrafo a partir
        do vértice v.

        Parâmetros:
        ----------
        v:
            - Vértice.
        visited:
            - Lista de vértices já visitados.
        parent:
            - Pai do vértice atual.

        Retorno:
        ----------
        True: se o subgrafo possuir um loop.

        False: caso não possua.
        """
        visited[v] = True

        for i in self.vertices:
            if(self.is_vertices_adjacents(v, i)):
                if visited[i] is False:
                    if(self.cycle(i, visited, v)):
                        return True
                elif parent != i:
                    return True
        return False

    def has_cycle(self):
        """
        Método que verifica se o grafo possui um ciclo.
        Loops também são detectados.

        Retorno:
        ----------
        True: se gráfo possuir ciclo ou loop.

        False: caso nao possua.
        """
        visited = dict()

        for i in self.vertices:
            visited[i] = False

        for i in self.vertices:
            if visited[i] is False:
                if(self.cycle(i, visited, -1)) is True:
                    return True
        return False

    def has_loop(self):
        """
        Método que verifica se o grafo possui um loop.

        Retorno:
        ----------
        True: se gráfo possuir loop.

        False: caso nao possua.
        """
        for edge in self.edges:
            if edge.is_loop():
                return True
        return False

    def check_regular_graph(self):
        """
        Método que verifica a regularidade de um grafo.

        Retorno:
        ----------
        True: Se o grafo for regular.

        False: Se o grafo não for regular.
        """
        valency = []

        for i in self.vertices:
            v = 0
            aux = SimpleVertex(i)
            for j in self.edges:
                if aux == j.vertex_a or aux == j.vertex_b:
                    v += 1
            valency.append(v)
        return len(set(valency)) <= 1

    def incidence_list(self):
        """
        Método que retorna uma lista de objetos que contem
        a incidencia dos vertices com as arestas.

        Retorno:
        ----------
        incidence_list: List
            - Lista com os objetos de ligação(ValueBinding).
        """
        incidence_list = []
        for v in self.vertices.values():
            for e in self.edges:
                if e.vertex_a == v and e.vertex_b == v:
                    incidence_list.append(
                        ValueBinding(v.get_value(), e.get_name(), 2)
                    )
                elif e.vertex_a == v or e.vertex_b == v:
                    incidence_list.append(
                        ValueBinding(v.get_value(), e.get_name(), 1)
                    )
                else:
                    incidence_list.append(
                        ValueBinding(v.get_value(), e.get_name(), 0)
                    )
        return incidence_list

    def adjacency_matrix(self):
        """
        Método que retorna a representação em forma de
        matriz de adjacência do grafo.

        Retorno:
        ----------
        adjacency_matrix: Dict
            - Dicionario que representa o grafo no formato
            matriz de adjacência.
        """
        adjacency_matrix = dict()
        for value in self.vertices.keys():
            adjacency_matrix[value] = dict()

            for vertex in self.vertices.keys():
                adjacency_matrix[value][vertex] = 0

        for edge in self.edges:
            value_a = edge.vertex_a.get_value()
            value_b = edge.vertex_b.get_value()
            adjacency_matrix[value_a][value_b] += 1
            adjacency_matrix[value_b][value_a] += 1

        return adjacency_matrix

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
