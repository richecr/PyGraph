from ..py_graph_t.SimpleGraph import SimpleGraph


class TestSimpleGraph:
    graph = SimpleGraph()

    def test_num_vertex(self):
        self.graph.add_vertex("a")
        assert self.graph.num_vertex() == 1
