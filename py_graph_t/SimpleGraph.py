from .vertex.SimpleVertex import SimpleVertex
from .edges.SimpleEdge import SimpleEdge

from .exceptions.SimpleGraphException import VertexNotExistsException, EdgeDuplicatedException, EdgeNotFoundException, VertexDuplicatedException


class SimpleGraph:
    """Implementação de um simples grafo."""
    vertices = dict()
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
        if not self.vertices.__contains__(value):
            self.vertices[value] = SimpleVertex(value)
            return self.vertices[value]
        else:
            raise VertexDuplicatedException()

    def delete_vertex(self, value):
        """
        Método que remove um vertice do grafo e consequentemente todas as arestas
        conectadas ao vertice.

        Parâmetros:
        ----------
        value: *
            - identificador do vértice a ser removido
        """

        vertex_removed = self.vertices[value]
        if self.vertex_exists(value):
            for i in range(len(self.edges)-1, -1, -1):
                edge = self.edges[i]
                if self.is_terminal(edge, value):
                    self.edges.pop(i)

            self.vertices.__delitem__(value)
        
        return vertex_removed

    def show_edge(self, value_a, value_b):
        """
        Método que retorna uma aresta entre dois vértices, se ela existe.

        Parâmetros:
        ----------
        value_a: *
            - identificador do vértice.
        value_b: *
            - identificador do vértice.
        """
        
        vertex_a = self.vertices.get(value_a)
        vertex_b = self.vertices.get(value_b)
        
        if vertex_a is None or vertex_b is None:
            raise VertexNotExistsException
        
        edge_test = SimpleEdge(vertex_a=vertex_a, vertex_b=vertex_b)      

        for edge in self.edges:
            if edge_test.__eq__(edge):
                return edge

    def add_edge(self, value_a, value_b, name=None):
        """
        Método que adiciona uma aresta ao grafo.

        Parâmetros:
        ----------
        value_a: *
            - Identificador do vértice cabeça da aresta.
        value_b: *.
            - Identificador do vértice cauda da aresta.
        name: String
            - Nome da aresta do grafo.
        """
        
        vertex_a = self.vertices.get(value_a)
        vertex_b = self.vertices.get(value_b)

        if vertex_a is None or vertex_b is None:
            raise VertexNotExistsException()
        if SimpleEdge(name=name, vertex_a=vertex_a, vertex_b=vertex_b) in self.edges:
            raise EdgeDuplicatedException()
        else:
            self.edges.append(SimpleEdge(name=name, vertex_a=vertex_a, vertex_b=vertex_b))
            return self.show_edge(value_a, value_b)

    def delete_edge(self, value_a, value_b):
        """
        Método que remove uma aresta do grafo.

        Parâmetros:
        ----------
        value_a: *
            - Identificador do vértice cabeça da aresta.
        value_b: *.
            - Identificador do vértice cauda da aresta.
        """
        vertex_a = self.vertices.get(value_a)
        vertex_b = self.vertices.get(value_b)
        edge_aux = SimpleEdge(vertex_a=vertex_a, vertex_b=vertex_b)
        
        if self.edges.__contains__(edge_aux):
            self.edges.remove(edge_aux)
            return edge_aux
        else:
            raise EdgeNotFoundException()

    def is_terminal(self, edge, value):
        """
        Método que verifica se um dado vértice é terminal de uma dada aresta.
        
        Parâmetros:
        ----------
            edge: SimpleEdge
                - Aresta a ser verificada.
            vertex: *
                - identificador do vertice.
        
        Retorno:
        ----------
        resultado: bool
            - Valor booleano indicando se o vértice é um dos terminais da aresta.
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
        value: *
            - identificador do vértice a ser verificado

        Retorno:
        ----------
        True: Caso o vertice pertença ao grafo.

        False: Caso não.
        """
        return self.vertices.__contains__(value)

    def edge_exists(self, value_a, value_b):
        """
        Método booleano que indica se um determinada aresta pertence ao Grafo.

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
        value: *
            - identificador do vertice.
        
        Retorno:
        ----------
        neigh_vertices: List
            - Lista de vertices.
        """
        neigh_vertices = []
        
        for edge in self.edges:
            if edge.vertex_a.value == value:
                neigh_vertices.append(edge.vertex_b)
            elif edge.vertex_b.value == value:
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
        if self.vertex_exists(value):
            return len(self.vertex_neighbors(value))
        else:
            raise VertexNotExistsException()
    
    def is_vertices_adjacents(self, value_a, value_b):
        """
        Método que indica se os vértices de entrada são adjacentes.

        Parâmetros:
        ----------
        value_a: *
            - identificador do vértice.
        value_b: *
            - identificador do vértice.
        
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
        Método que retorna lista com todos os identificadores dos vértices do grafo.

        Retorno:
        ----------
        vertices: lista com o nome de todas os vértices do grafo.
        """
        vertices = []
        for vertex in self.vertices:
            vertices.append(vertex)
        return vertices

    def list_graph_edges(self):
        """
        Método que retorna lista com todos os nomes as arestas do grafo.
        
        Retorno:
        ----------
        edges: lista com o nome de todas as arestas do grafo.
        """
        edges = []
        for edge in self.edges:
            edges.append(edge.name)
        return edges
    

    def cycle(self, v, visited, parent):
        """
        Método que verifica se tem ciclo no subgrafo a partir do vértice v.

        Parâmetros:
        ----------
        v: *
            - Vértice.
        visited: *
            - Lista de vértices já visitados.
        parent: *
            - Pai do vértice atual.
        
        Retorno:
        ----------
        True: se o subgrafo possuir um loop.

        False: caso não possua.
        """
        visited[v]= True

        for i in self.vertices: 
            if(self.is_vertices_adjacents(v,i)):
                if  visited[i] == False :  
                    if(self.cycle(i, visited, v)): 
                        return True
                elif  parent != i: 
                    return True

        return False

    def has_loop(self): 
        """
        Método que verifica se o grafo possui um loop/ciclo.

        Retorno:
        ----------
        True: se gráfo possuir loop/ciclo.

        False: caso nao possua.
        """
        visited = dict()

        for i in self.vertices:
            visited[i] = False

        for i in self.vertices: 
            if visited[i] == False: 
                if(self.cycle(i, visited, -1)) == True: 
                    return True

        return False
        
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
    
    def check_regular_graph(self):
        """
        Função que verifica a regularidade de um grafo.

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

