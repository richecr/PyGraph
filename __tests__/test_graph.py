import pytest

from ..py_graph_t.Graph import Graph
from ..py_graph_t.util.ValueBinding import ValueBinding
from ..py_graph_t.edges.SimpleEdge import SimpleEdge
from ..py_graph_t.vertex.SimpleVertex import SimpleVertex
from ..py_graph_t.exceptions.SimpleGraphException import (
    VertexDuplicatedException,
    VertexNotExistsException,
    EdgeNotFoundException,
    EdgeNameExistsException
)


@pytest.fixture
def simple_graph():
    g = Graph()
    g.vertices = dict()
    g.edges = []
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    g.add_edge("a", "b", name="s")
    g.add_edge("b", "c", name="t")
    g.add_edge("a", "a", name="d")
    return g


class TestGraph:
    g = Graph()

    def test_add_vertex(self, simple_graph):
        simple_graph.add_vertex("e")
        assert simple_graph.vertex_exists("e") is True
        assert "e" in simple_graph.get_all_vertex().keys()

    def test_exception_add_vertex_duplicate(self, simple_graph):
        with pytest.raises(VertexDuplicatedException):
            assert simple_graph.add_vertex("a")

    def test_delete_vertex(self, simple_graph):
        num_vertex = simple_graph.num_vertex()
        simple_graph.add_vertex("e")
        v = simple_graph.delete_vertex("e")
        assert v.__str__() == "Vértice e"
        assert simple_graph.num_vertex() == num_vertex

    def test_exception_delete_vertex_not_exists(self, simple_graph):
        with pytest.raises(VertexNotExistsException):
            assert simple_graph.delete_vertex("e")

    def test_delete_vertex_terminal(self, simple_graph):
        simple_graph.delete_vertex("a")
        expected = 1
        assert simple_graph.num_edges() == expected

    def test_show_edge(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        edge_zx = simple_graph.add_edge("z", "x", "zx")
        edge_test = SimpleEdge("zx", vertex_z, vertex_x)
        assert simple_graph.show_edge("z", "x") == edge_test

    def test_exception_show_edge_vertex_not_exists(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        with pytest.raises(VertexNotExistsException):
            assert simple_graph.show_edge("z", "x")

    def test_exception_show_edge_not_exists(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        with pytest.raises(EdgeNotFoundException):
            assert simple_graph.show_edge("z", "x")

    def test_add_edge(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        assert simple_graph.add_edge("z", "x", "zx") == \
            SimpleEdge("zx", vertex_z, vertex_x)

    def test_exception_add_edge_vertex_not_exists(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = SimpleVertex("x")
        with pytest.raises(VertexNotExistsException):
            assert simple_graph.add_edge("z", "x", "zx") == \
                SimpleEdge("zx", vertex_z, vertex_x)

    def test_exception_add_edge_name_exists(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        with pytest.raises(EdgeNameExistsException):
            assert simple_graph.add_edge("z", "x", "d") == \
                SimpleEdge("zx", vertex_z, vertex_x)

    def test_delete_edge(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        edge_test = simple_graph.add_edge("z", "x", "zx")
        assert simple_graph.delete_edge("z", "x") == edge_test

    def test_delete_edge(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        edge_test = simple_graph.add_edge("z", "x", "zx")
        assert simple_graph.delete_edge("z", "x") == edge_test

    def test_exception_delete_edge_not_exists(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        with pytest.raises(EdgeNotFoundException):
            assert simple_graph.delete_edge("z", "x")

    def test_is_terminal(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        edge_test = simple_graph.add_edge("z", "x", "zx")
        assert simple_graph.is_terminal(edge_test, "z") is True
        assert simple_graph.is_terminal(edge_test, "x") is True
        assert simple_graph.is_terminal(edge_test, "a") is False

    def test_num_vertex(self, simple_graph):
        assert simple_graph.num_vertex() == 3
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        assert simple_graph.num_vertex() == 5
        simple_graph.delete_vertex("z")
        simple_graph.delete_vertex("x")
        assert simple_graph.num_vertex() == 3

    def test_vertex_exists(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        assert simple_graph.vertex_exists("a") is True
        assert simple_graph.vertex_exists("z") is True
        assert simple_graph.vertex_exists("x") is False

    def test_edge_exists(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        edge_test = simple_graph.add_edge("z", "x", "zx")
        assert simple_graph.edge_exists("z", "x") is True

    def test_edge_not_exists(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        assert simple_graph.edge_exists("z", "a") is False

    def test_num_edges(self, simple_graph):
        assert simple_graph.num_edges() == 3
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        edge_test = simple_graph.add_edge("z", "x", "zx")
        assert simple_graph.num_edges() == 4
        simple_graph.delete_edge("z", "x")
        assert simple_graph.num_edges() == 3

    def test_vertex_neighbors(self, simple_graph):
        vertex_a = SimpleVertex("a")
        vertex_b = SimpleVertex("b")
        expected = [vertex_b, vertex_a]
        assert simple_graph.vertex_neighbors("a") == expected

    def test_exception_vertex_neighbors_vertex_not_exists(self, simple_graph):
        with pytest.raises(VertexNotExistsException):
            assert simple_graph.vertex_neighbors("z")

    def test_vertex_degree(self, simple_graph):
        assert simple_graph.vertex_degree("a") == 2

    def test_exception_vertex_degree_vertex_not_exists(self, simple_graph):
        with pytest.raises(VertexNotExistsException):
            assert simple_graph.vertex_degree("z")

    def test_is_vertices_adjacents(self, simple_graph):
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        assert simple_graph.is_vertices_adjacents("a", "b") is True
        assert simple_graph.is_vertices_adjacents("z", "x") is False

    def test_exception_is_vertices_adjacents_not_exists(self, simple_graph):
        vertex_x = simple_graph.add_vertex("x")
        with pytest.raises(VertexNotExistsException):
            assert simple_graph.is_vertices_adjacents("z", "x")

    def test_get_all_vertex(self, simple_graph):
        vertex_a = SimpleVertex("a")
        vertex_b = SimpleVertex("b")
        vertex_c = SimpleVertex("c")
        expected = {"c": vertex_c, "b": vertex_b, "a": vertex_a}
        assert simple_graph.get_all_vertex() == expected

    def test_list_graph_vertices(self, simple_graph):
        expected = ["a", "b", "c"]
        assert simple_graph.list_graph_vertices() == expected

    def test_list_graph_edges(self, simple_graph):
        expected = ["s", "t", "d"]
        assert simple_graph.list_graph_edges() == expected

    def test_has_cycle(self, simple_graph):
        simple_graph.delete_edge("a", "a")
        vertex_z = simple_graph.add_vertex("z")
        vertex_x = simple_graph.add_vertex("x")
        simple_graph.add_edge("z", "x", "zx")
        simple_graph.add_edge("z", "a", "za")
        simple_graph.add_edge("a", "x", "ax")
        assert simple_graph.has_cycle() is True

    def test_has_cycle_simples(self, simple_graph):
        assert simple_graph.has_cycle() is True
        simple_graph.delete_edge("a", "a")
        assert simple_graph.has_cycle() is False

    def test_has_loop(self, simple_graph):
        assert simple_graph.has_loop() is True
        simple_graph.delete_edge("a", "a")
        assert simple_graph.has_cycle() is False

    def test_check_regular_graph(self, simple_graph):
        simple_graph.delete_edge("a", "a")
        simple_graph.add_edge("c", "a", "ca")
        assert simple_graph.check_regular_graph() is True

    def test_incidence_list(self, simple_graph):
        vb1 = ValueBinding("a", "s", 1)
        vb2 = ValueBinding("a", "t", 0)
        vb3 = ValueBinding("a", "d", 2)

        vb4 = ValueBinding("b", "s", 1)
        vb5 = ValueBinding("b", "t", 1)
        vb6 = ValueBinding("b", "d", 0)

        vb7 = ValueBinding("c", "s", 0)
        vb8 = ValueBinding("c", "t", 1)
        vb9 = ValueBinding("c", "d", 0)
        expected = [vb1, vb2, vb3, vb4, vb5, vb6, vb7, vb8, vb9]
        assert simple_graph.incidence_list() == expected

    def test_incidence_list_should_return_a_list(self, simple_graph):
        list_ = simple_graph.incidence_list()
        expected = True
        assert isinstance(list_, list) == expected

    def test_incidence_list_length(self, simple_graph):
        vertices_len = len(simple_graph.vertices)
        edges_len = len(simple_graph.edges)
        expected = vertices_len * edges_len
        result = len(simple_graph.incidence_list())
        assert expected == result

    def test_adjacency_matrix_should_return_dict(self, simple_graph):
        m = simple_graph.adjacency_matrix()
        expected = True
        assert isinstance(m, dict) == expected

    def test_adjacency_matrix_get_correct_vertexes(self, simple_graph):
        m = simple_graph.adjacency_matrix()
        vertexes = m.keys()
        assert list(vertexes) == ["a", "b", "c"]

    def test_adjacency_matrix_get_correct_edges(self, simple_graph):
        m = simple_graph.adjacency_matrix()
        edges = list(m.values())
        edges_a = edges[0]
        edges_b = edges[1]
        edges_c = edges[2]

        assert edges_a["a"] == int(simple_graph.edge_exists("a", "a"))*2
        assert edges_b["b"] == int(simple_graph.edge_exists("b", "b"))*2
        assert edges_c["c"] == int(simple_graph.edge_exists("c", "c"))*2
        assert edges_a["b"] == edges_b["a"]
        assert edges_a["c"] == edges_c["a"]
        assert edges_b["c"] == edges_c["b"]
