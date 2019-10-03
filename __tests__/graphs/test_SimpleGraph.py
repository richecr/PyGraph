from py_graph_t.SimpleGraph import SimpleGraph

grafo = SimpleGraph()

def teste():
    grafo.add_vertex("a")
    assert grafo.num_vertex() == 1