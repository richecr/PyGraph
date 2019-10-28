import pytest

from ..py_graph_t.SimpleGraph import SimpleGraph
from ..py_graph_t.exceptions.SimpleGraphException import (
    VertexNotExistsException,
    EdgeDuplicatedException,
    EdgeNotFoundException,
    VertexDuplicatedException,
    CycleDetectedException
)
from ..py_graph_t.Graph import Graph
from ..py_graph_t.util.ValueBinding import ValueBinding

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

    def teste(self, simple_graph):
        list_ = simple_graph.incidence_list()
        test = ValueBinding("a", "s", 1)
        assert list_[0].__eq__(test)

    def test_incidence_list_should_return_a_list(self, simple_graph):
        list_ = simple_graph.incidence_list()
        expected = True
        assert isinstance(list_, list) == expected

    def test_incidence_list_should_have_len_equal_number_edges_times_number_vertex(self, simple_graph):
        vertices_len = len(simple_graph.vertices)
        edges_len = len(simple_graph.edges)
        expected = vertices_len * edges_len
        result = len(simple_graph.incidence_list())
        assert expected == result


