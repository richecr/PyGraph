import pytest

from ..py_graph_t.SimpleGraph import SimpleGraph
from ..py_graph_t.exceptions.SimpleGraphException import VertexNotExistsException, EdgeDuplicatedException, EdgeNotFoundException, VertexDuplicatedException, CycleDetectedException
from ..py_graph_t.Graph import Graph
from ..py_graph_t.util.ValueBinding import ValueBinding


class TestGraph:
    g = Graph()

    def teste(self):
        g = Graph()
        g.vertices = dict()
        g.edges = []
        g.add_vertex("a")
        g.add_vertex("b")
        g.add_vertex("c")
        g.add_edge("a", "b", name="s")
        g.add_edge("b", "c", name="t")
        g.add_edge("a", "a", name="d")
        list_ = g.incidence_list()
        test = ValueBinding("a", "s", 1)
        assert list_[0].__eq__(test)    