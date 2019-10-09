from ..py_graph_t.SimpleGraph import SimpleGraph


class TestSimpleGraph:
    graph = SimpleGraph()

    def test_num_vertex(self):
        self.graph.add_vertex("a")
        assert self.graph.num_vertex() == 1

    def test_add_vertex(self):
        value = "a"
        self.graph.add_vertex(value)
        print(self.graph.vertices[value])
        assert str(self.graph.vertices[value]) == 'Vértice a'

    def test_delete_vertex(self):
        self.graph.add_vertex("a")
        self.graph.delete_vertex("a")
        assert self.graph.num_vertex() == 0

    def test_is_terminal(self):
        self.graph.delete_vertex("a")
        self.graph.add_vertex("a")
        self.graph.add_edge("a", "a", "a")
        assert self.graph.edges[0].vertex_a.value == "a" or self.graph.edges[0].vertex_b.value == "a"

    def test_vertex_exists(self):
        self.graph.delete_vertex("a")
        self.graph.add_vertex("a")
        assert self.graph.vertices.__contains__("a")

    def test_edge_exists(self):
        self.graph.delete_vertex("a")
        self.graph.add_vertex("a")
        self.graph.add_edge("a", "a", "a")
        assert self.graph.edges.__contains__(self.graph.edges[0])

    def test_num_edges(self):
        assert len(self.graph.edges) == len(self.graph.edges)

    def test_vertex_neighbors(self):
        for x in range(10):
            self.graph.add_vertex(str(x))
        for x in range(10):
            self.graph.add_edge("0", str(x), "x")
        assert str(self.graph.edges[-1]) == str('x: Vértice 0 -> Vértice 9')

    def test_vertex_degree(self):
        self.graph.add_vertex("b")
        assert len(self.graph.vertex_neighbors("b")) == 0

    def test_vertices_adjacency(self):
        self.graph.add_vertex("a")
        self.graph.add_vertex("b")
        self.graph.add_edge("a", "b", "x")
        neigh_vertices = self.graph.vertex_neighbors("a")
        vertex_b = self.graph.vertices.get("b")
        assert vertex_b in neigh_vertices

    def test_get_all_vertex(self):
        self.graph.vertices = dict()
        self.graph.add_vertex("a")
        assert str(self.graph.vertices['a']) == 'Vértice a'

    def test_list_graph_vertices(self):
        self.graph.vertices = dict()
        self.graph.add_vertex("a")
        vertices = []
        for vertex in self.graph.vertices:
            vertices.append(vertex)
        assert str(self.graph.vertices['a']) == 'Vértice a'

    def test_list_graph_edges(self):
        edges = []
        self.graph.edges = []
        self.graph.vertices = dict()
        self.graph.add_vertex("a")
        self.graph.add_vertex("b")
        self.graph.add_edge("a", "b", "x")
        for edge in self.graph.edges:
            edges.append(edge.name)
        assert edges == ['x']

    def test_show_edge(self):
        self.graph.edges = []
        self.graph.vertices = dict()
        self.graph.add_vertex("a")
        self.graph.add_vertex("b")
        self.graph.add_edge("a", "b", "x")
        assert str(self.graph.show_edge('a', 'b')) == str('x: Vértice a -> Vértice b')
        
    def test_true_loop_graph(self):
        self.graph.edges = []
        self.graph.vertices = dict()
        self.graph.add_vertex("a")
        self.graph.add_vertex("b")
        self.graph.add_vertex("c")
        self.graph.add_edge("a", "b", 1)
        self.graph.add_edge("b", "c", 2)
        self.graph.add_edge("c", "a", 3)
        assert self.graph.has_loop() == True

    def test_false_loop_graph(self):
        self.graph.edges = []
        self.graph.vertices = dict()
        self.graph.add_vertex("a")
        self.graph.add_vertex("b")
        self.graph.add_vertex("c")
        self.graph.add_vertex("d")
        self.graph.add_edge("a", "b", 1)
        self.graph.add_edge("b", "c", 2)
        self.graph.add_edge("c", "d", 3)
        assert self.graph.has_loop() == False