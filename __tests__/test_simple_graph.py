import pytest

from ..py_graph_t.SimpleGraph import SimpleGraph
from ..py_graph_t.exceptions.SimpleGraphException import (
    EdgeDuplicatedException,
    LoopDetectedException
)


class TestSimpleGraph:
    graph = SimpleGraph()

    def test_num_vertex(self):
        self.graph.add_vertex("a")
        assert self.graph.num_vertex() == 1

    def test_add_vertex(self):
        value = "b"
        vertex = self.graph.add_vertex(value)
        assert str(vertex) == 'Vértice b'

    def test_delete_vertex(self):
        vertex_delete = self.graph.delete_vertex("a")
        assert self.graph.num_vertex() == 1
        assert str(vertex_delete) == "Vértice a"

    def test_is_terminal(self):
        self.graph.add_vertex("a")
        self.graph.add_edge("a", "b", "ab")
        assert self.graph.edges[0].vertex_a.value == "a" or \
            self.graph.edges[0].vertex_b.value == "b"

    def test_vertex_exists(self):
        assert self.graph.vertex_exists("a")

    def test_edge_exists(self):
        assert self.graph.edge_exists("a", "b")

    def test_num_edges(self):
        assert self.graph.num_edges() == 1

    def test_vertex_neighbors(self):
        neighbors_true = []
        for x in range(10):
            self.graph.add_vertex(str(x))
        for x in range(1, 5):
            neighbors_true.append(self.graph.vertices[str(x)])
            self.graph.add_edge("0", str(x), "x")
        assert self.graph.vertex_neighbors("0") == neighbors_true

    def test_vertex_degree(self):
        assert len(self.graph.vertex_neighbors("b")) == 1

    def test_vertices_adjacency(self):
        neighbors_vertices = self.graph.vertex_neighbors("a")
        vertex_b = self.graph.vertices.get("b")
        assert vertex_b in neighbors_vertices

    def test_get_all_vertex(self):
        assert str(self.graph.get_all_vertex()) == "{'b': Vértice b, " + \
            "'a': Vértice a, '0': Vértice 0, '1': Vértice 1, " + \
            "'2': Vértice 2, '3': Vértice 3, '4': Vértice 4, " + \
            "'5': Vértice 5, '6': Vértice 6, '7': Vértice 7, " + \
            "'8': Vértice 8, '9': Vértice 9}"

    def test_list_graph_vertices(self):
        vertices = []
        for vertex in self.graph.vertices:
            vertices.append(vertex)
        assert str(self.graph.list_graph_vertices()) == \
            "['b', 'a', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']"

    def test_list_graph_edges(self):
        edges = []
        for edge in self.graph.edges:
            edges.append(edge.name)
        assert str(self.graph.list_graph_edges()) == \
            "['ab', 'x', 'x', 'x', 'x']"

    def test_show_edge(self):
        assert str(self.graph.show_edge('a', 'b')) == \
            str('ab: Vértice a -> Vértice b')

    def test_true_cycle_graph(self):
        self.graph.add_vertex("c")
        self.graph.add_edge("b", "c", 2)
        self.graph.add_edge("c", "a", 3)
        assert self.graph.has_cycle() is True
        assert self.graph.has_loop() is False

    def test_false_cycle_graph(self):
        self.graph.delete_edge("c", "a")
        self.graph.add_vertex("d")
        self.graph.add_edge("c", "d", 3)
        assert self.graph.has_cycle() is False
        assert self.graph.has_loop() is False

    def test_loop(self):
        with pytest.raises(LoopDetectedException):
            assert self.graph.add_edge("d", "d")
        assert self.graph.has_loop() is False

    def test_true_regular_graph(self):
        self.graph.delete_vertex("d")
        for i in range(0, 10):
            self.graph.delete_vertex(str(i))

        self.graph.add_vertex("d")
        self.graph.delete_edge("b", "c")
        self.graph.add_edge("c", "d", 3)
        print(self.graph.__str__())
        assert self.graph.check_regular_graph() is True

    def test_false_regular_graph(self):
        self.graph.add_edge("b", "c", 3)
        assert self.graph.check_regular_graph() is False

    def test_duplicated_edge(self):
        with pytest.raises(EdgeDuplicatedException):
            assert self.graph.add_edge("b", "c")
